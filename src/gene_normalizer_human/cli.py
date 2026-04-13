import argparse, os, pandas as pd
from .version import __version__
from .utils import parse_gtf_gene_map, load_hgnc_synonyms, split_multi_names
from .resolver import GeneResolver

def read_table(path: str):
    lower = path.lower()
    if lower.endswith('.xlsx') or lower.endswith('.xls'):
        return pd.read_excel(path, engine='openpyxl')
    if lower.endswith('.csv'):
        return pd.read_csv(path)
    if lower.endswith('.tsv') or lower.endswith('.txt'):
        try:
            return pd.read_csv(path, sep='\t')
        except Exception:
            return pd.read_csv(path)
    # default: one name per line
    return pd.read_csv(path, header=None, names=['original_gene_name'])

def app():
    p = argparse.ArgumentParser(prog='gene-normalizer-human', description='Human-only gene normalizer for Ensembl mapping.')
    p.add_argument('input', help='Input Excel/CSV/TSV file')
    p.add_argument('--col', default=None, help='Column containing gene names (default: auto-detect incl. original_gene_name)')
    p.add_argument('--gtf', required=True, help='Ensembl GTF (gz/plain)')
    p.add_argument('--hgnc', help='HGNC complete set TSV (optional)')
    p.add_argument('--split-delims', default='/,;|', help='Delimiters for multi-name cells (default: "/,;|")')
    p.add_argument('--no-fuzzy', action='store_true', help='Disable fuzzy matching')
    p.add_argument('-o','--out', default='mapped_genes.xlsx', help='Output .xlsx or .csv')
    p.add_argument('--keep-empty', action='store_true', help='Keep rows with no matched tokens')
    args = p.parse_args()

    df = read_table(args.input)
    col = args.col
    if col is None:
        for c in df.columns:
            if str(c).lower() in ('original_gene_name','gene','genes','symbol','hugo_symbol','hgnc_symbol'):
                col = c; break
        if col is None:
            col = df.columns[0]

    gene_name_to_ids, gene_id_to_name = parse_gtf_gene_map(args.gtf)
    syn = {}
    if args.hgnc and os.path.exists(args.hgnc):
        syn = load_hgnc_synonyms(args.hgnc)

    resolver = GeneResolver(gene_name_to_ids, gene_id_to_name, syn)

    rows = []
    for idx, val in enumerate(df[col].astype(str).tolist()):
        tokens = split_multi_names(val, delims=args.split_delims)
        token_results = [resolver.resolve_one(t, fuzzy=not args.no_fuzzy) for t in tokens]
        # 대표 선정 규칙: 우선순위 name-exact > synonym-exact > fuzzy-name > fuzzy-synonym > synonym-only > unmatched
        order = {'name-exact':0, 'synonym-exact':1, 'fuzzy-name':2, 'fuzzy-synonym':3, 'synonym-only':4, 'unmatched':5}
        best = None
        if token_results:
            best = sorted(token_results, key=lambda x: order.get(x['match_type'], 9))[0]
        if best is None and not args.keep_empty:
            continue
        # 요약 필드 구성
        matched_symbols = ';'.join(sorted(set([r['matched_symbol'] for r in token_results if r and r['matched_symbol']])))
        ensg_ids = ';'.join(sorted(set([r['ensembl_gene_id'] for r in token_results if r and r['ensembl_gene_id']])))
        rows.append({
            'row_index': idx,
            'original': val,
            'tokens': ';'.join(tokens),
            'representative_symbol': (best['matched_symbol'] if best else ''),
            'representative_ensembl_gene_id': (best['ensembl_gene_id'] if best else ''),
            'representative_match_type': (best['match_type'] if best else 'empty'),
            'all_matched_symbols': matched_symbols,
            'all_ensembl_gene_ids': ensg_ids
        })

    out_df = pd.DataFrame(rows, columns=[
        'row_index','original','tokens',
        'representative_symbol','representative_ensembl_gene_id','representative_match_type',
        'all_matched_symbols','all_ensembl_gene_ids'
    ])

    if args.out.lower().endswith('.csv'):
        out_df.to_csv(args.out, index=False)
    else:
        with pd.ExcelWriter(args.out, engine='openpyxl') as xw:
            out_df.to_excel(xw, index=False, sheet_name='mapped')
    print(f"[ok] {len(out_df)} rows -> {args.out}")
