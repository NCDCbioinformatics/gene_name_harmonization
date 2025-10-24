# gene-name-harmonization

#package download

#install
unzip gene-normalizer-human_0.2.0.zip \
cd gene_normalizer_human \
pip install -e .

#run package
gene-normalizer-human "/path/gene_normalizer_human_0.2.1/gene_name_test.xlsx" \
  --col original_gene_name \
  --gtf "/path/gene_normalizer_human_0.2.1/Homo_sapiens.GRCh38.110.gtf.gz" \
  --hgnc "/path/gene_normalizer_human_0.2.1/hgnc_complete_set.txt" \
  -o "/out_path/mapped.xlsx"

