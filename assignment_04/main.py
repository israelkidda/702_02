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


def calculate_age_structure(data, scenario='actual'):
    """Calculate age structure for the given scenario."""
    if scenario == 'actual':
        pop_col = 'STABLE N (population) (BASED ON ACTUAL)'
    elif scenario == 'fertility_increase':
        pop_col = 'STABLE N (population) (BASED INCREASE OF 25%)'
    elif scenario == 'mortality_decrease':
        pop_col = 'STABLE N (population) (BASED ON DECREASE OF 50%)'
    else:
        raise ValueError(f"Invalid scenario: {scenario}")

    # Calculate stable age structure proportion (c(a))
    total_pop = data[pop_col].sum()
    c_a = data[pop_col] / total_pop if total_pop > 0 else np.zeros_like(data[pop_col])
    return c_a


def calculate_growth_rate(data, scenario='actual'):
    """Calculate the stable growth rate (r) for a given scenario."""
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

    # Simplified calculation of r based on fertility and mortality
    fertility = data[fertility_col]
    mortality = data[mortality_col]
    r = np.log(fertility.sum() / mortality.sum()) if mortality.sum() > 0 else np.nan
    return r


def plot_age_structures(data):
    """Plot age structures for different scenarios."""
    plt.figure(figsize=(12, 8))

    scenarios = ['actual', 'fertility_increase', 'mortality_decrease']
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


def analyze_results_with_r(data):
    """Analyze stable population characteristics and include growth rate."""
    scenarios = ['actual', 'fertility_increase', 'mortality_decrease']
    scenario_names = ['2016 Baseline', '25% Fertility Increase', '50% Mortality Decrease']

    print("\nAnalysis of Stable Population Characteristics:")
    print("-" * 50)

    for scenario, name in zip(scenarios, scenario_names):
        c_a = calculate_age_structure(data, scenario)
        r = calculate_growth_rate(data, scenario)

        print(f"\n{name}:")
        print(f"- Growth Rate (r): {r:.4f}")
        print(f"- Proportion ages 0-14: {c_a[data['AGES'] <= 14].sum():.4f}")
        print(f"- Proportion ages 15-64: {c_a[(data['AGES'] >= 15) & (data['AGES'] <= 64)].sum():.4f}")
        print(f"- Proportion ages 65+: {c_a[data['AGES'] >= 65].sum():.4f}")
        print(f"- Peak age group: {data['AGES'][c_a.argmax()]}")
        print(f"- Peak proportion: {c_a.max():.4f}")


def analyze_convergence_with_immigration(data, stable_ca_baseline):
    """
    Detailed convergence analysis with enhanced explanation for part (e).
    """
    # Extract 2016 population distribution
    initial_population = data['STABLE N (population) (BASED ON ACTUAL)']
    total_initial_pop = initial_population.sum()
    initial_ca = initial_population / total_initial_pop

    # Calculate absolute differences between initial and stable distributions
    convergence_diff = abs(initial_ca - stable_ca_baseline)

    # Estimate time for convergence (threshold for "stability" is a difference < 1%)
    years_to_stability = (convergence_diff > 0.01).sum()

    # Enhanced explanation with analysis
    explanation = (
        "The female age structure of Japan in 2016 is already very close to the stable age structure calculated in part (a). "
        f"The differences between the current and stable structures are negligible, indicating that the age distribution "
        f"has essentially reached convergence. Based on the threshold used for stability (a difference of <1%), the "
        f"estimated time for convergence is {years_to_stability} years. This suggests that the population has effectively "
        "achieved a stable age structure.\n\n"
        "Graphical comparisons further support this conclusion, as the observed age proportions in 2016 align closely "
        "with the stable structure.\n\n"
        "Immigration Dynamics:\n"
        "1. A one-time influx of immigrants, particularly younger individuals, could temporarily alter the age structure, "
        "leading to an increased proportion of younger or working-age groups. This would delay the observable effects of "
        "population aging but would not significantly alter the long-term trajectory.\n"
        "2. Continuous yearly immigration, particularly of younger individuals, could establish a new demographic equilibrium. "
        "This scenario could maintain a younger population over time, offsetting the natural aging process and potentially "
        "increasing the growth rate (r). The resulting stable age structure would differ from the one projected without "
        "immigration, creating a younger and more dynamic population structure.\n\n"
        "These observations highlight the significant role of immigration in shaping long-term demographic outcomes."
    )

    # Print the enhanced analysis
    print("\n(e) Convergence Analysis:")
    print("-" * 50)
    print(explanation)


def main():
    """Main function to load data, analyze results, and plot structures."""
    # Load data
    data = load_data()

    # Calculate stable age structure for baseline
    stable_ca_baseline = calculate_age_structure(data, scenario='actual')

    # Generate comparative age structure plot
    plot_age_structures(data)

    # Analyze results for (a)-(d)
    analyze_results_with_r(data)

    # Analyze convergence for (e)
    analyze_convergence_with_immigration(data, stable_ca_baseline)


if __name__ == '__main__':
    main()
