import pandas as pd
import numpy as np

# Load your cleaned data
file_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/Stable Population Theory, Applications/cleaned_HW4_Japan.csv'
data = pd.read_csv(file_path)

def verify_growth_rate(data, scenario='actual'):
    """Standalone function to verify growth rate calculations."""
    if scenario == 'actual':
        fertility_col = '2016 AGE-SPECIFIC FERTILITY (BASED ON ACTUAL)'
        mortality_col = '2016 PROBABILITY OF DYING (BASED ON ACTUAL)'
    elif scenario == 'fertility_increase':
        fertility_col = '2016 AGE-SPECIFIC FERTILITY (BASED INCREASE OF 25%)'
        mortality_col = '2016 PROBABILITY OF DYING (BASED INCREASE OF 25%)'
    elif scenario == 'mortality_decrease':
        fertility_col = '2016 AGE-SPECIFIC FERTILITY (BASED ON DECREASE OF 50%)'
        mortality_col = '2016 PROBABILITY OF DYING (BASED ON DECREASE OF 50%)'
    else:
        raise ValueError(f"Invalid scenario: {scenario}")
    
    # Calculate fertility and mortality sums
    fertility_sum = data[fertility_col].sum()
    mortality_sum = data[mortality_col].sum()
    
    # Debugging output for manual verification
    print(f"\nVerification for Scenario: {scenario}")
    print(f"Fertility Sum: {fertility_sum}")
    print(f"Mortality Sum: {mortality_sum}")
    
    # Calculate growth rate
    r = np.log(fertility_sum / mortality_sum) if mortality_sum > 0 else np.nan
    print(f"Growth Rate (r): {r}\n")
    return r

# Verify growth rates for each scenario
scenarios = ['actual', 'fertility_increase', 'mortality_decrease']
for scenario in scenarios:
    verify_growth_rate(data, scenario)
