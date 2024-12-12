import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
def load_data(year):
    file_paths = {
        '1751': '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/Stable Population Theory, Applications/cleaned_1751.csv',
        '1900': '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/Stable Population Theory, Applications/cleaned_1900.csv',
        '2016': '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/Stable Population Theory, Applications/cleaned_2016.csv'
    }
    file_path = file_paths.get(year)
    if file_path:
        data = pd.read_csv(file_path)
        print(f"\nCleaned Data Loaded for {year}:")
        print(data.head())
        return data
    else:
        raise FileNotFoundError(f"Data for year {year} not found!")

# Plot the survival probability curve for each year
def plot_survival_curve(data, year):
    plt.figure(figsize=(10, 6))
    plt.plot(data['a'], data['p(a)'], label=f"Survival Probability, p(a) - {year}", marker='o')
    plt.title(f'Survival Probability Curve ({year})')
    plt.xlabel('Age (a)')
    plt.ylabel('Survival Probability, p(a)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Calculate Life Expectancy at Birth (e0)
def calculate_e0(data):
    data['weighted_p'] = data['p(a)'] * data['exp(-r*a)']
    e0 = data['weighted_p'].sum()
    return e0

# Critique section
def critique_assumptions():
    print("\nCritique of Stable Population Theory Assumptions:")

    # Assumption 1: Constant birth rates and mortality rates over time
    print("\n1. Constant Birth and Mortality Rates")
    print("   Stable population theory assumes constant birth and mortality rates over time. This assumption is not realistic,")
    print("   especially when considering the three different time periods (1751, 1900, and 2016), which are marked by")
    print("   significant socio-economic and medical changes. In 1751, Sweden was still under pre-industrial conditions,")
    print("   with high mortality rates due to infectious diseases, poor nutrition, and limited medical care.")
    print("   By 1900, Sweden was experiencing the early stages of industrialization, with improved public health measures.")
    print("   By 2016, the country had advanced healthcare systems, a high standard of living, and improved disease control.")
    
    # Assumption 2: Exponential growth of population
    print("\n2. Exponential Growth")
    print("   Another assumption of stable population theory is the exponential growth of populations. However, this does not")
    print("   accurately reflect historical patterns in Sweden. In 1751, population growth was slower and more volatile, with")
    print("   large swings due to wars, famines, and diseases. By 1900, growth was more consistent, but not exponential.")
    print("   In 2016, while Sweden had a relatively stable population growth rate, it was affected by immigration and policy changes.")
    
    # Assumption 3: No migration effects
    print("\n3. No Migration Effects")
    print("   Stable population theory generally assumes no migration, but in practice, migration has played a significant role")
    print("   in Swedish population dynamics, especially in the 20th and 21st centuries. Immigration, especially in the 2010s,")
    print("   has impacted the population size and structure, which is not considered in stable population theory.")
    
    # Conclusion
    print("\nIn conclusion, while stable population theory provides a useful framework for understanding long-term population trends,")
    print("it oversimplifies the complexities of demographic change over time. The assumptions of constant rates and exponential")
    print("growth do not hold in practice, particularly for historical periods such as 1751, 1900, and 2016.")

# Main code execution
def main():
    # Load data for each year
    data_1751 = load_data('1751')
    data_1900 = load_data('1900')
    data_2016 = load_data('2016')

    # Plot survival curves for each year
    plot_survival_curve(data_1751, '1751')
    plot_survival_curve(data_1900, '1900')
    plot_survival_curve(data_2016, '2016')

    # Calculate life expectancy for each year
    e0_1751 = calculate_e0(data_1751)
    e0_1900 = calculate_e0(data_1900)
    e0_2016 = calculate_e0(data_2016)

    # Print life expectancy results
    print(f"\nLife Expectancy at Birth for 1751 (e0): {e0_1751:.2f} years")
    print(f"Life Expectancy at Birth for 1900 (e0): {e0_1900:.2f} years")
    print(f"Life Expectancy at Birth for 2016 (e0): {e0_2016:.2f} years")

    # Run the critique of assumptions
    critique_assumptions()

if __name__ == '__main__':
    main()








































































































print()
print()
print()
print()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Path to cleaned data (provided by the user)
cleaned_data_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/Stable Population Theory, Applications/cleaned_data.csv'

# Load the dataset
df = pd.read_csv(cleaned_data_path)

# Inspect the first few rows to locate fertility and mortality rate columns
print("Columns in the dataset:")
print(df.columns)

# Sample fertility rates to ensure we're getting the correct data
print("Sample fertility rates:")
print(df['fertility rates by calendar year and age (Lexis squares, age in completed years (ACY))'].head())

# Extract fertility and mortality rates for the year 2016
# Assuming 'Period' column contains the year and 'fertility rates by calendar year and age (Lexis squares, age in completed years (ACY))' has the fertility rates
# Also assuming the mortality rate column is similarly structured

# Get the data for 2016 (filter by 'Period' == 2016)
df_2016 = df[df['Period'] == 2016]

# Extract necessary columns (replace with actual column names based on your data inspection)
fertility_column = 'fertility rates by calendar year and age (Lexis squares, age in completed years (ACY))'
mortality_column = '1qx'  # Update this with the correct mortality column name

# Calculate the stable population (simplified model)
def calculate_stable_population(fertility, mortality, age_groups):
    # Initialize population vectors (simplified, assuming initial equal distribution)
    population = np.ones(len(age_groups))
    
    # Apply fertility and mortality rates to estimate long-term stable population structure
    for i in range(1, len(age_groups)):
        population[i] = population[i-1] * (1 - mortality[i-1]) * fertility[i-1]
    
    return population / population.sum()  # Normalize to sum to 1 (stable structure)

# Apply the stable population function to the 2016 data
age_groups = df_2016['Age']  # Replace with the actual column for age groups
fertility_rates = df_2016[fertility_column].values
mortality_rates = df_2016[mortality_column].values

stable_population_2016 = calculate_stable_population(fertility_rates, mortality_rates, age_groups)

# If fertility increases by 25%, calculate the new stable population
fertility_rates_increased = fertility_rates * 1.25
stable_population_increased_fertility = calculate_stable_population(fertility_rates_increased, mortality_rates, age_groups)

# If mortality decreases by 50%, calculate the new stable population
mortality_rates_decreased = mortality_rates * 0.5
stable_population_decreased_mortality = calculate_stable_population(fertility_rates, mortality_rates_decreased, age_groups)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(age_groups, stable_population_2016, label='2016 Baseline', color='blue')
plt.plot(age_groups, stable_population_increased_fertility, label='Increased Fertility (25%)', color='green')
plt.plot(age_groups, stable_population_decreased_mortality, label='Decreased Mortality (50%)', color='red')

plt.xlabel('Age Groups')
plt.ylabel('Proportion of Population')
plt.title('Stable Population Age Structure for Japan (2016, Increased Fertility, Decreased Mortality)')
plt.legend()
plt.grid(True)
plt.show()

