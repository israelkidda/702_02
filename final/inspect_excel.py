import pandas as pd
import os

# File path for the input Excel file
input_file_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/final paper main/final final dec 19/final data/total_data.xlsx'

# Directory for the output file
output_dir = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/final paper main/final final dec 19/final data'

# Output file path
output_file_path = os.path.join(output_dir, 'clean_data.csv')

# Relevant column names
columns_of_interest = ['Time', 'Sex', 'Age', 'Value']

# Sheets to process
sheets = ['population', 'IMR', 'U5MR']

# Initialize an empty DataFrame to collect cleaned data
cleaned_data = pd.DataFrame()

# Function to clean and extract relevant data from a sheet
def clean_sheet(file_path, sheet_name):
    try:
        # Load the sheet using column names
        data = pd.read_excel(file_path, sheet_name=sheet_name, usecols=columns_of_interest, header=0)
        
        # Add a new column to indicate the sheet's data source
        data['Category'] = sheet_name
        
        # Preview the cleaned data for the current sheet
        print(f"\nCleaned data for sheet '{sheet_name}':")
        print(data.head())
        
        return data
    except Exception as e:
        print(f"Error processing sheet '{sheet_name}': {e}")
        return None

# Process each sheet and collect the cleaned data
for sheet in sheets:
    sheet_data = clean_sheet(input_file_path, sheet)
    if sheet_data is not None:
        cleaned_data = pd.concat([cleaned_data, sheet_data], ignore_index=True)

# Save the cleaned data to a CSV file
try:
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists
    cleaned_data.to_csv(output_file_path, index=False)
    print(f"\nCleaned data saved to: {output_file_path}")
except Exception as e:
    print(f"Error saving cleaned data: {e}")
