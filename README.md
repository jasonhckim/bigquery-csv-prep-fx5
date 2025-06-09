# FX5 Sales Report CSV Cleaner

This project provides a Python-based CSV cleaning pipeline designed to prepare FX5 sales report files for seamless ingestion into Google BigQuery. It ensures all parts follow a unified schema and that inconsistent values are normalized.

## 🧾 Features

- ✅ Uses the header from `part_1.csv` as a schema reference for all files.
- ✅ Replaces `NA` in the `DC Percent` column with `0.0` (for proper float conversion).
- ✅ Replaces `NA` in the `Paid Date` column with the value from `Invoice Date`.
- ✅ Strips problematic characters like quotes, commas, and newlines from all fields.
- ✅ Processes files in a memory-efficient streaming manner (suitable for large datasets).
- ✅ Outputs cleaned CSV files ready for upload to BigQuery.

---

## 📂 Directory Structure

```
fx5-sales-data-cleaning/
├── clean_fx5_sales_data.py   # Main script
├── part_1.csv                # Source file with reference header
├── part_11.csv to part_27.csv  # Input part files
├── fx5_sales_11_final_corrected.csv  # Output cleaned files
└── README.md                 # This file
```

---

## 🧪 Requirements

- Python 3.6+
- Works in Google Colab or any standard Python environment

---

## 🚀 How to Use

1. Upload `part_1.csv` and the desired input files (e.g., `part_11.csv` to `part_27.csv`) into your Colab or working directory.
2. Set the `input_output_files` list to match your target files.
3. Run the script:

```python
# Example setup for file processing
input_output_files = [
    ("part_11.csv", "fx5_sales_11_final_corrected.csv"),
    ...
    ("part_27.csv", "fx5_sales_27_final_corrected.csv"),
]
```

4. The cleaned CSV files will be saved and ready for download or BigQuery ingestion.

---

## 🧹 Field Sanitization Logic

Each field is sanitized as follows:

- All double quotes `"` and commas `,` are removed.
- Newlines and carriage returns (`\n`, `\r`) are replaced with spaces.
- `NA` values in specific columns are substituted:
  - `DC Percent` → `0.0`
  - `Paid Date` → value from `Invoice Date`

---

## 📦 Output Format

Output files are named using the convention:

```
fx5_sales_<part number>_final_corrected.csv
```

Each file contains clean, schema-aligned rows safe for ingestion into BigQuery.

---

## 📜 License

This project is intended for internal or analytical use. Please include appropriate credits if reused externally.

---

## 🤝 Contributions

Feel free to submit issues or enhancements. Pull requests are welcome if adapting this for broader ETL workflows.

[README.md](https://github.com/user-attachments/files/20662378/README.md)
