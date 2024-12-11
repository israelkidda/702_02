import pandas as pd
import os

# File path to the HW4 Japan Excel file
file_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/Stable Population Theory, Applications, HW4 Japan.xlsx'

# Load the sheet without assuming headers
sheet_name = 'HW4 Japan'  # You might need to adjust this sheet name based on the actual one in the file
raw_data = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

# Display the first few rows to understand the structure of the data
print("\nInitial Inspection of Raw Data:")
print(raw_data.head(20))

# Step 1: Automatically detect the header row
def detect_header_row(data):
    potential_headers = data.apply(lambda row: row.astype(str).str.match(r"[a-zA-Z]").any(), axis=1)
    header_candidates = data[potential_headers]
    most_unique_values = header_candidates.apply(lambda row: row.nunique(), axis=1)
    header_row_index = most_unique_values.idxmax()
    return header_row_index

header_row_index = detect_header_row(raw_data)
print(f"\nDetected Header Row Index: {header_row_index}")

# Step 2: Use the detected row as the header
data = pd.read_excel(file_path, sheet_name=sheet_name, header=header_row_index)

# Step 3: Clean column names
data.columns = data.columns.astype(str).str.strip()  # Strip any extra spaces from column names
data = data.loc[:, ~data.columns.duplicated()]  # Remove duplicate columns

# Step 4: Extract relevant columns (you'll need to update this based on the actual structure)
columns_of_interest = ['a', '1qx', 'fertility_rate', 'other_columns_if_needed']
missing_columns = [col for col in columns_of_interest if col not in data.columns]
if missing_columns:
    print(f"\nError: Missing expected columns: {missing_columns}")
    print(f"Available columns: {list(data.columns)}")
    exit(1)

data_cleaned = data[columns_of_interest]
print("\nExtracted Relevant Data:")
print(data_cleaned.head())

# Step 5: Save the cleaned data to a new CSV file for later use in main.py
output_dir = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/Stable Population Theory, Applications'
output_file = os.path.join(output_dir, 'cleaned_HW4_Japan.csv')
os.makedirs(output_dir, exist_ok=True)
data_cleaned.to_csv(output_file, index=False)

print(f"\nCleaned data saved to: {output_file}")
