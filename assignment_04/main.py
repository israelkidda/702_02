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
print('PROBLEM TWO')
print()
print()
print()
print()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    """Load the corrected cleaned Japan data."""
    file_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/major homeworks/04 dec 18/Stable Population Theory, Applications/cleaned_HW4_Japan.csv'
    data = pd.read_csv(file_path)
    print(f"Loaded Data:\n{data.head()}")
    print(f"\nColumn Names:\n{list(data.columns)}")
    return data

def calculate_age_structure(data, column_name):
    """Calculate age structure for the given column."""
    total_pop = data[column_name].sum()
    c_a = data[column_name] / total_pop if total_pop > 0 else np.zeros_like(data[column_name])
    return c_a

def plot_age_structures(data):
    """Plot age structures for different scenarios."""
    plt.figure(figsize=(12, 8))

    scenarios = ['STABLE N (population) (BASED ON ACTUAL)',
                 'STABLE N (population) (BASED INCREASE OF 25%)',
                 'STABLE N (population) (BASED ON DECREASE OF 50%)']
    labels = ['2016 Baseline', '25% Fertility Increase', '50% Mortality Decrease']
    colors = ['blue', 'green', 'red']

    for scenario, label, color in zip(scenarios, labels, colors):
        c_a = calculate_age_structure(data, scenario)
        plt.plot(data['AGES'], c_a, label=label, color=color, alpha=0.7)

    plt.title('Comparative Stable Age Structures')
    plt.xlabel('Age')
    plt.ylabel('Proportion of Population (c(a))')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("\n(d) Analysis of c(a) and r:")
    print("The stable age structure c(a) differs across scenarios due to varying fertility and mortality assumptions:")
    print("1. Higher fertility (25% increase) results in a younger age structure, with higher proportions at younger ages.")
    print("2. Reduced mortality (50% decrease) leads to an older age structure, with significant proportions at older ages.")
    print("3. Growth rate (r) differs accordingly, with higher fertility increasing r and reduced mortality decreasing r.")

def analyze_results_with_r(data):
    """Analyze stable population characteristics and include growth rate."""
    scenarios = [
        ('STABLE N (population) (BASED ON ACTUAL)', '2016 AGE-SPECIFIC FERTILITY (BASED ON ACTUAL)', '2016 PROBABILITY OF DYING (BASED ON ACTUAL)'),
        ('STABLE N (population) (BASED INCREASE OF 25%)', '2016 AGE-SPECIFIC FERTILITY (BASED INCREASE OF 25%)', '2016 PROBABILITY OF DYING (BASED INCREASE OF 25%)'),
        ('STABLE N (population) (BASED ON DECREASE OF 50%)', '2016 AGE-SPECIFIC FERTILITY (BASED ON DECREASE OF 50%)', '2016 PROBABILITY OF DYING (BASED ON DECREASE OF 50%)')
    ]
    scenario_names = ['2016 Baseline', '25% Fertility Increase', '50% Mortality Decrease']

    print("\nAnalysis of Stable Population Characteristics:")
    print("-" * 50)

    for (pop_col, fertility_col, mortality_col), name in zip(scenarios, scenario_names):
        c_a = calculate_age_structure(data, pop_col)
        fertility = data[fertility_col]
        mortality = data[mortality_col]
        r = np.log(fertility.sum() / mortality.sum()) if mortality.sum() > 0 else np.nan

        print(f"\n{name}:")
        print(f"- Growth Rate (r): {r:.4f}")
        print(f"- Proportion ages 0-14: {c_a[data['AGES'] <= 14].sum():.4f}")
        print(f"- Proportion ages 15-64: {c_a[(data['AGES'] >= 15) & (data['AGES'] <= 64)].sum():.4f}")
        print(f"- Proportion ages 65+: {c_a[data['AGES'] >= 65].sum():.4f}")
        print(f"- Peak age group: {data['AGES'][c_a.argmax()]}")
        print(f"- Peak proportion: {c_a.max():.4f}")

def analyze_convergence_with_immigration(data):
    """Detailed convergence analysis for part (e)."""
    current_population = data['CURRENT POPULATION OF JAPAN (FEMALES ONLY) N(a,t)']
    stable_population = data['STABLE POPULATION OF JAPAN (FEMALES ONLY) N(a,t)']

    current_ca = calculate_age_structure(data, 'CURRENT POPULATION OF JAPAN (FEMALES ONLY) N(a,t)')
    stable_ca = calculate_age_structure(data, 'STABLE POPULATION OF JAPAN (FEMALES ONLY) N(a,t)')

    # Calculate differences
    differences = abs(current_ca - stable_ca)
    max_diff_age = data.loc[differences.idxmax(), 'AGES']
    max_diff_value = differences.max()

    # Estimate time to convergence
    years_to_stability = (differences > 0.01).sum()

    print("\n(e) Convergence Analysis:")
    print("-" * 50)
    print("The current age structure (Column Q) is compared to the stable age structure (Column R).")
    print(f"Largest Difference: At age {max_diff_age}, there’s a difference of {max_diff_value:.4%} between the current and stable structures.")
    print(f"Time to Convergence: It will take approximately {years_to_stability} years for the population to stabilize, assuming no major changes in fertility, mortality, or immigration.\n")

    print("Immigration Dynamics:")
    print("1. A one-time influx of younger immigrants would temporarily increase the proportion of younger age groups, delaying convergence slightly.")
    print("2. Continuous yearly immigration could maintain a younger population and create a new demographic equilibrium, fundamentally altering the stable age structure.\n")

    print("Takeaways:")
    print("Japan’s population is aging and shrinking due to low fertility and high life expectancy.")
    print("Increasing fertility or encouraging immigration could slow or alter this trend.")
    print("Without intervention, it will take about 59 years for the population to stabilize, but this stable structure will still reflect an aging society with a significant elderly population.")

    # Plot comparison of current vs. stable age structures
    plt.figure(figsize=(12, 8))
    plt.plot(data['AGES'], current_ca, label='Current Population (2016)', color='blue', alpha=0.7)
    plt.plot(data['AGES'], stable_ca, label='Stable Population', color='red', alpha=0.7)
    plt.fill_between(data['AGES'], current_ca, stable_ca, color='gray', alpha=0.3, label='Differences')
    plt.title('Current vs. Stable Population Proportions (Females Only)')
    plt.xlabel('Age')
    plt.ylabel('Proportion of Population')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    """Main function to load data, analyze results, and plot structures."""
    # Load data
    data = load_data()

    # Generate comparative age structure plot
    plot_age_structures(data)

    # Analyze results for (a)-(d)
    analyze_results_with_r(data)

    # Analyze convergence for (e)
    analyze_convergence_with_immigration(data)

if __name__ == '__main__':
    main()
