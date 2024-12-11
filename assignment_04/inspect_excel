import pandas as pd
import os

# File paths for the three years
file_paths = {
    '1751': '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/YEAR 1751_Stable Population Theory, Applications, HW4 Sweden.xlsx',
    '1900': '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/YEAR 1990_Stable Population Theory, Applications, HW4 Sweden.xlsx',
    '2016': '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/YEAR 2016_Stable Population Theory, Applications, HW4 Sweden.xlsx'
}

# Function to clean data for a given file
def clean_data(file_path):
    # Load the sheet without assuming headers
    raw_data = pd.read_excel(file_path, sheet_name='HW4 Sweden (females)', header=None)

    # Step 1: Automatically detect the header row
    def detect_header_row(data):
        potential_headers = data.apply(lambda row: row.astype(str).str.match(r"[a-zA-Z]").any(), axis=1)
        header_candidates = data[potential_headers]
        most_unique_values = header_candidates.apply(lambda row: row.nunique(), axis=1)
        header_row_index = most_unique_values.idxmax()
        return header_row_index

    header_row_index = detect_header_row(raw_data)

    # Step 2: Use the detected row as the header
    data = pd.read_excel(file_path, sheet_name='HW4 Sweden (females)', header=header_row_index)

    # Step 3: Clean column names
    data.columns = data.columns.astype(str).str.strip()
    data = data.loc[:, ~data.columns.duplicated()]  # Remove duplicate columns

    # Step 4: Extract relevant columns
    columns_of_interest = ['a', 'N(a,t)', 'B(t)', 'r', 'exp(-r*a)', 'p(a)']
    missing_columns = [col for col in columns_of_interest if col not in data.columns]
    if missing_columns:
        print(f"\nError: Missing expected columns in {file_path}: {missing_columns}")
        print(f"Available columns: {list(data.columns)}")
        return None

    data_cleaned = data[columns_of_interest]
    return data_cleaned

# Clean data for each year (1751, 1900, 2016)
data_1751 = clean_data(file_paths['1751'])
data_1900 = clean_data(file_paths['1900'])
data_2016 = clean_data(file_paths['2016'])

# Check if any data is missing
if data_1751 is None or data_1900 is None or data_2016 is None:
    print("Error: One or more years have missing data.")
    exit(1)

# Save the cleaned data for each year to CSV files
output_dir = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/Stable Population Theory, Applications'
os.makedirs(output_dir, exist_ok=True)

# Save the cleaned data for each year
data_1751.to_csv(os.path.join(output_dir, 'cleaned_1751.csv'), index=False)
data_1900.to_csv(os.path.join(output_dir, 'cleaned_1900.csv'), index=False)
data_2016.to_csv(os.path.join(output_dir, 'cleaned_2016.csv'), index=False)

print("\nCleaned data for 1751, 1900, and 2016 saved to CSV.")
