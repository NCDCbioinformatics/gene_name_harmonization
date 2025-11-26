# gene-name-harmonization
#install \
unzip gene-normalizer-human_0.2.0.zip \
cd gene_normalizer_human \
pip install -e .

#run package \
gene-normalizer-human "/path/gene_normalizer_human_0.2.1/gene_name_test.xlsx" \
  --col original_gene_name \
  --gtf "/path/gene_normalizer_human_0.2.1/Homo_sapiens.GRCh38.110.gtf.gz" \
  --hgnc "/path/gene_normalizer_human_0.2.1/hgnc_complete_set.txt" \
  -o "/out_path/mapped.xlsx"

# Summary features
Read the `original_gene_name` column from Excel/CSV/TSV \
Separation and normalization using delimiters (`/, ; |`) etc. \
Mapping Ensembl gene_name / gene_id to Ensembl GTF + HGNC synonyms

# main options
- `--col` : Input gene column name (default: auto-detect)
- `--gtf` : Ensembl GTF (gz/plain)
- `--hgnc`: HGNC TSV (symbol, alias_symbol, prev_symbol)
- `--split-delims` : Name separator (default: `/,;|`)
- `--no-fuzzy`
- `--keep-empty`
