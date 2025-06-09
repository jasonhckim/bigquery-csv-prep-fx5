# FX5 Sales Report CSV Cleaner

This script is designed to clean and standardize multiple parts of FX5 sales report files for BigQuery ingestion.

## Purpose

1. **Standardize Headers**:
   - All files should use the same header as the first row of `part_1.csv`.

2. **Clean Data Fields**:
   - Replace any 'NA' in the `DC Percent` column with 0 and ensure it's a numeric field.
   - Replace any 'NA' in the `Paid Date` column with the corresponding value in `Invoice Date`.

## How to Use

1. Upload the `part_1.csv` and all other part files (e.g., `part_11.csv` to `part_20.csv`) to your Google Colab session.
2. Copy and paste the Python script into a code cell in Colab.
3. Execute the script.
4. Cleaned files will be saved with the naming format `fx5_sales_<part number>_final_corrected.csv`.

These cleaned files can now be reliably uploaded to Google BigQuery without data parsing issues.
