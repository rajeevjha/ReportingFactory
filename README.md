# Reporting Factory on Databricks (Starter Project)

This project provides a modular, extensible template for building a Reporting Factory using Databricks, DLT, and DAB.

## Features
- Ingestion pipelines (S3)
- Processing + enrichment
- Schema validation
- Report generation
- Report certification
- Report catalog

## Setup
1. Configure `databricks.yml` with your workspace.
2. Run DAB deploy & pipelines.
3. Use notebooks for certification & report generation.

## Deploy Commands
```bash
databricks bundle deploy
databricks bundle run s3_ingestion
```
