import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.stats.stattools import durbin_watson

# Load the cleaned data
file_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/final paper main/final final dec 19/final data/clean_data.csv'
data = pd.read_csv(file_path)

# Filter data for IMR and U5MR
mortality_data = data[data['Category'].isin(['IMR', 'U5MR'])]

# Add intervention column
mortality_data['intervention'] = (mortality_data['Time'] >= 1995).astype(int)

# Define a function for ITSA analysis
def run_itsa(data, outcome, category):
    data = data[data['Category'] == category]
    
    results = {}
    for sex in data['Sex'].unique():
        # Subset data by sex
        subset = data[data['Sex'] == sex].copy()
        subset['time_post'] = subset['Time'] - 1995
        subset['time_post'] = subset['time_post'].clip(lower=0)  # Set to 0 pre-intervention
        
        # Define the regression model
        X = sm.add_constant(subset[['Time', 'intervention', 'time_post']])
        y = subset['Value']
        model = sm.OLS(y, X).fit()
        
        # Store results
        results[sex] = {
            'model': model,
            'summary': model.summary(),
            'dw_stat': durbin_watson(model.resid),  # Durbin-Watson test for autocorrelation
            'predicted': model.predict(X),
        }
        
        # Visualization
        plt.figure(figsize=(10, 6))
        plt.plot(subset['Time'], subset['Value'], label='Observed', marker='o')
        plt.plot(subset['Time'], results[sex]['predicted'], label='Predicted', linestyle='--')
        plt.axvline(x=1995, color='red', linestyle=':', label='Intervention (1995)')
        plt.title(f'{category} Analysis - {sex}')
        plt.xlabel('Year')
        plt.ylabel(outcome)
        plt.legend()
        plt.grid()
        plt.show()
        
        print(f"\n{category} - {sex}: Durbin-Watson statistic = {results[sex]['dw_stat']}")
        print(results[sex]['summary'])

# Run ITSA for IMR and U5MR
print("\nRunning ITSA for IMR...")
run_itsa(mortality_data, 'Infant Mortality Rate (IMR)', 'IMR')

print("\nRunning ITSA for U5MR...")
run_itsa(mortality_data, 'Under-Five Mortality Rate (U5MR)', 'U5MR')
