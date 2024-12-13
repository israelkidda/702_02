import pandas as pd

# File path for the Excel document
file_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/_MY PROBELM TWO DATA.xlsx'

# Function to inspect and clean the Excel file
def inspect_and_clean_excel(file_path):
    try:
        # Load the data assuming the first row contains column names
        data = pd.read_excel(file_path, sheet_name='Sheet1')

        # Print the first few rows
        print("\nFirst 5 Rows of Data:")
        print(data.head())

        # Print column names
        print("\nColumn Names:")
        print(list(data.columns))

        # Convert numeric columns to appropriate data types
        data_cleaned = data.copy()
        for col in data_cleaned.columns:
            try:
                data_cleaned[col] = pd.to_numeric(data_cleaned[col], errors='coerce')
            except Exception as e:
                print(f"Error converting column {col}: {e}")

        # Print data types
        print("\nData Types After Conversion:")
        print(data_cleaned.dtypes)

        # Print summary statistics
        print("\nSummary Statistics:")
        print(data_cleaned.describe(include='all'))

        # Save cleaned data to a new CSV file for further analysis
        cleaned_file_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/Stable Population Theory, Applications/cleaned_HW4_Japan.csv'
        data_cleaned.to_csv(cleaned_file_path, index=False)
        print(f"\nCleaned data saved to: {cleaned_file_path}")

    except Exception as e:
        print(f"An error occurred while inspecting the file: {e}")

# Run the inspection and cleaning process
inspect_and_clean_excel(file_path)
