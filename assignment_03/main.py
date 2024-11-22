# Import required libraries
print("Starting program...")  # Debug print

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

print("Libraries imported successfully")  # Debug print

def load_and_prepare_data(file_path, start_row, end_row):
    """Load and prepare mortality data from Excel file"""
    print("\nSingle Decrement Life Tables for Egypt 2019")
    print("Source: WHO Mortality Database")
    print("====================================")
    
    data = pd.read_excel(file_path)
    egypt_2019_data = data.iloc[start_row-1:end_row]
    
    females_data = egypt_2019_data[egypt_2019_data['Sex'] == 1]
    males_data = egypt_2019_data[egypt_2019_data['Sex'] == 2]
    
    death_cols = [f'Deaths{i}' for i in range(1, 26)]
    females_ndx = females_data[death_cols].sum().values
    males_ndx = males_data[death_cols].sum().values
    
    return females_ndx, males_ndx

def construct_life_table(nDx, initial_population=100000):
    """Construct life table with demographic calculations"""
    age_groups = ['0', '1-4'] + [f"{5*i}-{5*(i+1)-1}" for i in range(1, 18)] + ['95+']
    
    if len(nDx) > len(age_groups):
        nDx = nDx[:len(age_groups)]
    
    n = len(age_groups)
    lx = np.zeros(n)
    dx = np.zeros(n)
    qx = np.zeros(n)
    px = np.zeros(n)
    Lx = np.zeros(n)
    Tx = np.zeros(n)
    ex = np.zeros(n)
    
    scale_factor = initial_population / sum(nDx)
    dx = np.array(nDx) * scale_factor
    
    lx[0] = initial_population
    for i in range(1, n):
        lx[i] = lx[i-1] - dx[i-1]
    
    for i in range(n):
        if lx[i] > 0:
            qx[i] = dx[i] / lx[i]
            px[i] = 1 - qx[i]
    
    for i in range(n):
        if i == 0:
            Lx[i] = lx[i] - dx[i]/2
        else:
            Lx[i] = 5 * (lx[i] - dx[i]/2) if i < n-1 else lx[i] / 2
    
    for i in range(n-1, -1, -1):
        Tx[i] = Lx[i] + (Tx[i+1] if i+1 < n else 0)
    
    for i in range(n):
        if lx[i] > 0:
            ex[i] = Tx[i] / lx[i]
    
    return pd.DataFrame({
        'Age Group': age_groups,
        'lx': lx.round(2),
        'dx': dx.round(2),
        'qx': qx.round(4),
        'px': px.round(4),
        'Lx': Lx.round(2),
        'Tx': Tx.round(2),
        'ex': ex.round(2)
    })

def plot_life_table_metrics(females_table, males_table):
    """Create separate visualizations for life table metrics"""
    age_groups = females_table['Age Group'].values
    x_positions = np.arange(len(age_groups))
    
    # Create four separate figures
    plt.figure(figsize=(10, 8))
    plt.plot(x_positions, females_table['px'], label='Females', color='red')
    plt.plot(x_positions, males_table['px'], label='Males', color='blue')
    plt.title('Probability of Surviving (px) - Egypt 2019')
    plt.xlabel('Age Group')
    plt.ylabel('Probability')
    plt.xticks(x_positions[::2], age_groups[::2], rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    plt.figure(figsize=(10, 8))
    plt.plot(x_positions, females_table['qx'], label='Females', color='red')
    plt.plot(x_positions, males_table['qx'], label='Males', color='blue')
    plt.title('Probability of Dying (qx) - Egypt 2019')
    plt.xlabel('Age Group')
    plt.ylabel('Probability')
    plt.xticks(x_positions[::2], age_groups[::2], rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    plt.figure(figsize=(10, 8))
    plt.plot(x_positions, females_table['lx'], label='Females', color='red')
    plt.plot(x_positions, males_table['lx'], label='Males', color='blue')
    plt.title('Number of Survivors (lx) - Egypt 2019')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Survivors')
    plt.xticks(x_positions[::2], age_groups[::2], rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    plt.figure(figsize=(10, 8))
    plt.plot(x_positions, females_table['ex'], label='Females', color='red')
    plt.plot(x_positions, males_table['ex'], label='Males', color='blue')
    plt.title('Life Expectancy (ex) - Egypt 2019')
    plt.xlabel('Age Group')
    plt.ylabel('Years')
    plt.xticks(x_positions[::2], age_groups[::2], rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

print("Functions defined successfully")  # Debug print

# Main execution
if __name__ == "__main__":
    try:
        print("\nExecuting main program...")  # Debug print
        
        # File path and parameters
        file_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/03 nov 20/mortality_data.xlsx'
        start_row = 7684
        end_row = 9479
        
        # Load and process data
        print("\nLoading data...")  # Debug print
        females_ndx, males_ndx = load_and_prepare_data(file_path, start_row, end_row)
        
        # Construct life tables
        print("\nConstructing life tables...")  # Debug print
        females_table = construct_life_table(females_ndx)
        males_table = construct_life_table(males_ndx)
        
        # Display results
        print("\nFemale Life Table - Egypt 2019:")
        print("============================")
        print(tabulate(females_table, headers='keys', tablefmt='grid', floatfmt=".4f"))
        
        print("\nMale Life Table - Egypt 2019:")
        print("==========================")
        print(tabulate(males_table, headers='keys', tablefmt='grid', floatfmt=".4f"))
        
        # Generate plots
        print("\nGenerating plots...")  # Debug print
        plot_life_table_metrics(females_table, males_table)
        
        print("\nProgram completed successfully")  # Debug print
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        import traceback
        traceback.print_exc()


















































    # New analysis code added at the end of the file
print("\nPerforming additional mortality pattern analysis...")

def calculate_survival_probabilities(life_table, target_ages=[15, 30, 45, 60, 75, 85]):
    """Calculate probability of surviving from birth to specific ages"""
    results = {}
    initial_lx = life_table['lx'].iloc[0]
    
    for age in target_ages:
        # Find the row corresponding to the target age
        age_row = life_table[life_table['Age Group'].str.contains(f'^{age}|^{age}-')].iloc[0]
        prob_survival = age_row['lx'] / initial_lx
        results[age] = prob_survival
    
    return results

def calculate_mortality_ratios(females_table, males_table):
    """Calculate mortality sex ratios (male/female) for different metrics"""
    ratios = {
        'qx_ratio': males_table['qx'] / females_table['qx'],
        'ex_ratio': males_table['ex'] / females_table['ex']
    }
    return pd.DataFrame(ratios, index=females_table['Age Group'])

# Calculate survival probabilities
female_survival = calculate_survival_probabilities(females_table)
male_survival = calculate_survival_probabilities(males_table)

# Calculate mortality ratios
mortality_ratios = calculate_mortality_ratios(females_table, males_table)

# Print detailed analysis
print("\nDETAILED MORTALITY PATTERN ANALYSIS")
print("===================================")

print("\n1. Survival Probabilities from Birth")
print("------------------------------------")
for age in female_survival.keys():
    print(f"Probability of surviving to age {age}:")
    print(f"Females: {female_survival[age]:.4f} ({female_survival[age]*100:.1f}%)")
    print(f"Males: {male_survival[age]:.4f} ({male_survival[age]*100:.1f}%)")
    diff = (female_survival[age] - male_survival[age]) * 100
    print(f"Difference (F-M): {diff:.1f} percentage points\n")

print("\n2. Life Expectancy Analysis")
print("---------------------------")
print(f"Life expectancy at birth:")
print(f"Females: {females_table['ex'].iloc[0]:.1f} years")
print(f"Males: {males_table['ex'].iloc[0]:.1f} years")
print(f"Gender gap: {females_table['ex'].iloc[0] - males_table['ex'].iloc[0]:.1f} years")

# Analysis at age 60
idx_60 = females_table[females_table['Age Group'] == '60-64'].index[0]
print(f"\nLife expectancy at age 60:")
print(f"Females: {females_table['ex'].iloc[idx_60]:.1f} years")
print(f"Males: {males_table['ex'].iloc[idx_60]:.1f} years")
print(f"Gender gap: {females_table['ex'].iloc[idx_60] - males_table['ex'].iloc[idx_60]:.1f} years")

print("\n3. Key Mortality Findings")
print("-------------------------")
# Infant and early childhood mortality
print(f"Infant mortality (qx at age 0):")
print(f"Females: {females_table['qx'].iloc[0]:.4f} ({females_table['qx'].iloc[0]*100:.1f}%)")
print(f"Males: {males_table['qx'].iloc[0]:.4f} ({males_table['qx'].iloc[0]*100:.1f}%)")

# Calculate peak mortality difference
mortality_diff = abs(males_table['qx'] - females_table['qx'])
max_diff_idx = mortality_diff.idxmax()
max_diff_age = females_table['Age Group'].iloc[max_diff_idx]

print(f"\nLargest mortality difference observed in age group {max_diff_age}:")
print(f"Females: {females_table['qx'].iloc[max_diff_idx]:.4f}")
print(f"Males: {males_table['qx'].iloc[max_diff_idx]:.4f}")

print("\n4. Hypotheses for Observed Patterns")
print("---------------------------------")
print("1. Gender-based biological differences:")
print("   - Higher male mortality rates likely reflect biological vulnerabilities")
print("   - Hormonal differences may contribute to female longevity advantage")

print("\n2. Behavioral and social factors:")
print("   - Male mortality patterns may reflect higher risk-taking behavior")
print("   - Occupational hazards may disproportionately affect males")
print("   - Different healthcare-seeking behaviors between genders")

print("\n3. Cultural and socioeconomic context:")
print("   - Gender roles in Egyptian society may influence mortality patterns")
print("   - Access to healthcare may vary by gender")
print("   - Traditional family structures may affect health-seeking behaviors")

print("\n5. Caveats and Limitations")
print("-------------------------")
print("1. Data quality considerations:")
print("   - Possible underreporting or misclassification of deaths")
print("   - Age heaping may affect accuracy of age-specific mortality rates")

print("\n2. Methodological limitations:")
print("   - Period life table assumes constant mortality conditions")
print("   - Does not account for cohort effects or temporal changes")

print("\n3. Contextual limitations:")
print("   - Analysis doesn't account for regional variations within Egypt")
print("   - Socioeconomic differentials not captured in the data")
print("   - Limited information on cause-specific mortality")

print("\nAdditional analysis completed successfully")