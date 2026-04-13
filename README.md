# gene-name-harmonization
<img width="2554" height="915" alt="image" src="https://github.com/user-attachments/assets/e42141a3-d222-48f8-84a0-71f3d6ef6b02" />

#install \
unzip gene-normalizer-human_0.2.1.zip \
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
## Publication context

This repository is a component of the CURE-NGS panel harmonization framework described in the manuscript \"Multi-Institutional Harmonization Framework for Heterogeneous Panel-Based NGS in Precision Oncology.\"

Umbrella repository: https://github.com/NCDCbioinformatics/cure-ngs-panel-harmonization-framework

## Software metadata

- Operating system(s): Linux or macOS; Windows users can run the package in a compatible Python environment
- Programming language(s): Python
- License: MIT License
