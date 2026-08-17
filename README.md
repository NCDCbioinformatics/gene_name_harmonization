# gene_name_harmonization

GTF/HGNC-backed gene-symbol normalization component of the CURE-NGS panel
harmonization framework.

> **Supported deployment:** use the unified
> [CURE-NGS Docker/OCI distribution](https://github.com/NCDCbioinformatics/cure-ngs-panel-harmonization-framework).
> This repository preserves component provenance. The one supported container
> is published from the umbrella repository, not this component repository;
> **No packages published** here is therefore expected.

## Role in the unified project

| Item | Value |
| --- | --- |
| Historical responsibility | Map current, alias, previous, and Ensembl gene identifiers to canonical symbols |
| Supported command | `cure-ngs normalize-gene` |
| Latest audited release | `gene_normalizer_human` / release name `gene_normalizer_human_0.2.1` |
| Required data | GTF containing `gene_id`/`gene_name` and HGNC complete-set TSV |

## Install the supported Docker distribution

Install [Docker Desktop](https://docs.docker.com/desktop/) or
[Docker Engine](https://docs.docker.com/engine/install/), then build:

```bash
git clone https://github.com/NCDCbioinformatics/cure-ngs-panel-harmonization-framework.git
cd cure-ngs-panel-harmonization-framework
docker build --file docker/Dockerfile.core --tag cure-ngs-harmonizer:0.1.0-core .
```

After release `0.1.0` is visible in the umbrella **Packages** panel:

```bash
docker pull ghcr.io/ncdcbioinformatics/cure-ngs-harmonizer:0.1.0-core
```

If no package is listed yet, use the source build above.

## Verify and run this capability

The reviewer walkthrough checks that the alias `P53` resolves to `TP53`:

```bash
bash scripts/run_reviewer_demo.sh
```

Direct component command with the bundled non-biological fixtures:

```bash
docker run --rm \
  --volume "$PWD/examples:/examples:ro" \
  cure-ngs-harmonizer:0.1.0-core normalize-gene P53 \
  --gtf /examples/synthetic/genes.gtf \
  --hgnc /examples/synthetic/hgnc.tsv
```

Institutional runs should mount a recorded GENCODE/Ensembl GTF and HGNC
complete-set snapshot. Fuzzy matching is disabled by default.

## Historical standalone package

The `gene_normalizer_human_0.2.1` release asset remains available for
provenance. It accepts Excel/CSV/TSV input and `--gtf`, `--hgnc`, `--col`,
`--split-delims`, `--no-fuzzy`, and `--keep-empty` options. The asset filename
is labelled 0.2.1 while its archived internal package metadata reports 0.2.0;
the umbrella lock records that discrepancy explicitly.

## Documentation and test data

- [Project structure](https://github.com/NCDCbioinformatics/cure-ngs-panel-harmonization-framework/blob/main/docs/PROJECT_STRUCTURE.md)
- [Gene/fusion commands](https://github.com/NCDCbioinformatics/cure-ngs-panel-harmonization-framework/blob/main/docs/COMMAND_REFERENCE.md#gene-and-fusion-normalization)
- [GTF and HGNC setup](https://github.com/NCDCbioinformatics/cure-ngs-panel-harmonization-framework/blob/main/docs/REFERENCE_DATA.md#4-install-gtf-and-hgnc-resources)
- [Synthetic GTF/HGNC fixtures](https://github.com/NCDCbioinformatics/cure-ngs-panel-harmonization-framework/tree/main/examples/synthetic)

License: MIT. No CURE-NGS patient-level data are distributed here.
