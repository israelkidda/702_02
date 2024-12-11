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
