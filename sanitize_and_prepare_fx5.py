import csv

# Redefine the sanitization function for streaming
def sanitize_field(field: str) -> str:
    return field.replace('"', '').replace(',', '').replace('\n', ' ').replace('\r', ' ').strip()

# Streaming approach for large files
cleaned_paths = []
for input_file, output_file in input_output_files:
    input_path = f"/mnt/data/{input_file}"
    output_path = f"/mnt/data/{output_file}"
    cleaned_paths.append(output_path)

    with open(input_path, 'r', encoding='ISO-8859-1', newline='') as infile, \
         open(output_path, 'w', encoding='utf-8', newline='') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)

        next(reader)  # Skip original header
        writer.writerow(reference_header)

        for row in reader:
            if len(row) == len(reference_header):
                row_dict = dict(zip(reference_header, row))

                if row_dict.get('DC Percent', '').strip().upper() == 'NA':
                    row_dict['DC Percent'] = '0.0'
                if row_dict.get('Paid Date', '').strip().upper() == 'NA':
                    row_dict['Paid Date'] = row_dict.get('Invoice Date', '')

                cleaned_row = [sanitize_field(row_dict.get(col, '')) for col in reference_header]
                writer.writerow(cleaned_row)

cleaned_paths
