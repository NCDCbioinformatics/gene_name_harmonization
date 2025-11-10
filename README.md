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

# 기능 요약
엑셀/CSV/TSV의 `original_gene_name` 열을 읽음 \
구분자(`/ , ; |`) 등으로 분리·정규화 \
Ensembl GTF + HGNC synonyms 로 Ensembl gene_name / gene_id를 매핑

# 주요 옵션
- `--col` : 입력 유전자 열 이름 (기본: auto-detect)
- `--gtf` : Ensembl GTF (gz/plain)
- `--hgnc`: HGNC TSV (symbol, alias_symbol, prev_symbol)
- `--split-delims` : 이름 분리 구분자 (기본: `/,;|`)
- `--no-fuzzy` : 퍼지 매칭 비활성화
- `--keep-empty` : 비어있는 결과도 출력(기본은 제외)
