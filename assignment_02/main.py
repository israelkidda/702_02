import textwrap

print("Israel Kidda")
print("DCP70200/SOC81900/QMSS750")
print("Methods of Demographic Analysis Fall 2024, CUNY Graduate Center")
print()
print("Assignment 2")
print()

print(textwrap.dedent("""\
    1. On Blackboard (same folder as this assignment) you will find a spreadsheet with
    (single-year) cohort age-specific fertility rates for women in the US, Canada, and Spain
    (Birth Cohorts 1921 and later). Do the following:
    """))
print()
print(textwrap.dedent("""\
    (a) Calculate the Total Fertility Rate in each country for the following four birth cohorts: 
        1921, 1936, 1951, 1966 (12 values in total).
    """))










import pandas as pd

# Step 1: Load the Excel data into a pandas DataFrame, specifying the header row
file_path = '/Users/israelmarykidda/Documents/Workspace_702_02/assignment_02/HW2_Q1_data.xlsx'
df = pd.read_excel(file_path, header=2)

# Step 2: Strip column names of any leading/trailing spaces and print column names to verify
df.columns = df.columns.str.strip()  # This removes any hidden spaces in the headers
print(df.columns)

# Step 3: Filter the data for the relevant birth cohorts (replace 'Birth Cohort' with 'Cohort')
cohorts = [1921, 1936, 1951, 1966]
filtered_df = df[df['Cohort'].isin(cohorts)]  # Corrected the column name to 'Cohort'

# Step 4: Group by cohort and sum ASFR for each country
tfr = filtered_df.groupby('Cohort').agg({
    'ASFR': 'sum',      # For USA
    'ASFR.1': 'sum',    # For Canada
    'ASFR.2': 'sum'     # For Spain
}).reset_index()

# Step 5: Rename the columns to reflect that we're now calculating TFR
tfr.columns = ['Cohort', 'USA TFR', 'Canada TFR', 'Spain TFR']

print()

# Step 6: Print the general expression for TFR
print("General formula for Total Fertility Rate (TFR):")
print("TFR = Σ (ASFR_x) for x = 15 to 49")

print()

# Step 7: Print the results directly to the terminal
print(tfr)










print()
print(textwrap.dedent("""\
    (b) Graph the age-specific fertility rates of the 1936 birth cohorts. Show the three graphs 
        (one for each country). Comment on any similarities and differences of cohort age-specific fertility 
        in the three countries. Start by analyzing the peaks and the degree of dispersion of the 
        distributions and relate it to differences in fertility timing. (Note that the area underneath each 
        curve equals the cohort TFR calculated in (a).) When making cross-country comparisons, also think 
        about the post-WW2 context in each country and recall that we already saw in class that the 1936 US 
        women were the peak Baby Boom (parent) cohort.
    """))










import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Print the general formula for Age-Specific Fertility Rate (ASFR)
print("General formula for Age-Specific Fertility Rate (ASFR):")
print("ASFR_x = (Number of births to women of age x) / (Number of women of age x)")

print()

# Step 2: Load the Excel data into a pandas DataFrame
file_path = '/Users/israelmarykidda/Documents/Workspace_702_02/assignment_02/HW2_Q1_data.xlsx'
df = pd.read_excel(file_path, header=2)

# Step 3: Filter the data for the 1936 cohort
df_1936 = df[df['Cohort'] == 1936]

# Step 4: Plot the ASFR for each country on a single graph
plt.figure(figsize=(10, 6))

# Plot USA ASFR
plt.plot(df_1936['Year'], df_1936['ASFR'], label='USA', color='blue', marker='o')

# Plot Canada ASFR
plt.plot(df_1936['Year'], df_1936['ASFR.1'], label='Canada', color='green', marker='s')

# Plot Spain ASFR
plt.plot(df_1936['Year'], df_1936['ASFR.2'], label='Spain', color='red', marker='^')

# Customize the plot
plt.title('Age-Specific Fertility Rates for 1936 Birth Cohort')
plt.xlabel('Year')
plt.ylabel('Age-Specific Fertility Rate')
plt.legend()  # Show legend to differentiate between countries
plt.grid(True)

# Display the plot
plt.show()

# Step 5: Add analysis of the graph in the terminal output
print()
print("Analysis of the Age-Specific Fertility Rate (ASFR) graph:")
print("1. The USA and Canada exhibit similar patterns with a sharp peak in ASFR during the late 1950s to early 1960s,")
print("   reflecting the so-called Baby Boom that occurred post-World War II.")
print("2. Spain's fertility rates are more spread out and peak slightly later, indicating a broader distribution of births")
print("   across ages, likely due to Spain's different post-war socio-economic context.")
print("3. All countries show a decline in fertility rates after their respective peaks, but the decline for Spain is more")
print("   gradual compared to the sharper decline in the USA and Canada.")
print("4. The area under the curve for each country correlates with the Total Fertility Rate (TFR) calculated earlier.")










print()
print(textwrap.dedent("""\
    (c) For each country separately, prepare a chart of the differences in the cumulative age-specific cohort 
        fertility rate of the 1921, 1951, and 1966 cohorts relative to the 1936 cohort (make 1936 the 
        baseline). Comment in detail on the within-country (cross-cohort) evidence regarding timing 
        differences (including any evidence of fertility postponement, i.e., delay of fertility from younger 
        to older ages). See slide 15, lecture 5 for an example.
    """))










import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Print the general formula for Cumulative ASFR
print("General formula for Cumulative Age-Specific Fertility Rate (Cumulative ASFR):")
print("Cumulative ASFR_x = Σ (ASFR_i) from i = 15 to x")
print()  # Add spacing for readability

# Step 2: Load the Excel data into a pandas DataFrame
file_path = '/Users/israelmarykidda/Documents/Workspace_702_02/assignment_02/HW2_Q1_data.xlsx'
df = pd.read_excel(file_path, header=2)

# Step 3: Filter the data for the relevant cohorts
cohorts = [1921, 1951, 1966, 1936]
df_filtered = df[df['Cohort'].isin(cohorts)]

# Step 4: Define a function to calculate cumulative ASFR
def calculate_cumulative_asfr(df, country_column):
    df = df.copy()  # Ensure we are working with a copy
    df.loc[:, 'Cumulative_ASFR'] = df[country_column].cumsum()  # Use loc to prevent warnings
    return df

# Step 5: Calculate cumulative ASFR for each country and each cohort
cumulative_asfr = {}
countries = ['ASFR', 'ASFR.1', 'ASFR.2']  # USA, Canada, Spain

for country in countries:
    cumulative_asfr[country] = {}
    for cohort in cohorts:
        df_cohort = df_filtered[df_filtered['Cohort'] == cohort]
        cumulative_asfr[country][cohort] = calculate_cumulative_asfr(df_cohort, country)['Cumulative_ASFR'].values

# Step 6: Align the arrays by using the minimum length of years (this ensures all arrays are the same size)
min_length = min([len(cumulative_asfr['ASFR'][1936]), len(cumulative_asfr['ASFR'][1921]), len(cumulative_asfr['ASFR'][1951]), len(cumulative_asfr['ASFR'][1966])])

# Step 7: Calculate the difference relative to the 1936 cohort for each country (align arrays)
differences = {}
for country in countries:
    differences[country] = {}
    baseline_1936 = cumulative_asfr[country][1936][:min_length]  # Truncate to the minimum length
    for cohort in [1921, 1951, 1966]:
        differences[country][cohort] = cumulative_asfr[country][cohort][:min_length] - baseline_1936

# Step 8: Plot the differences for each country
fig, axs = plt.subplots(3, 1, figsize=(10, 12))

# USA
axs[0].plot(df_filtered[df_filtered['Cohort'] == 1921]['Year'][:min_length], differences['ASFR'][1921], label='1921 Cohort', color='blue', marker='o')
axs[0].plot(df_filtered[df_filtered['Cohort'] == 1951]['Year'][:min_length], differences['ASFR'][1951], label='1951 Cohort', color='green', marker='s')
axs[0].plot(df_filtered[df_filtered['Cohort'] == 1966]['Year'][:min_length], differences['ASFR'][1966], label='1966 Cohort', color='red', marker='^')
axs[0].set_title('USA: Cumulative ASFR Difference Relative to 1936')
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Difference in Cumulative ASFR')
axs[0].legend()
axs[0].grid(True)

# Canada
axs[1].plot(df_filtered[df_filtered['Cohort'] == 1921]['Year'][:min_length], differences['ASFR.1'][1921], label='1921 Cohort', color='blue', marker='o')
axs[1].plot(df_filtered[df_filtered['Cohort'] == 1951]['Year'][:min_length], differences['ASFR.1'][1951], label='1951 Cohort', color='green', marker='s')
axs[1].plot(df_filtered[df_filtered['Cohort'] == 1966]['Year'][:min_length], differences['ASFR.1'][1966], label='1966 Cohort', color='red', marker='^')
axs[1].set_title('Canada: Cumulative ASFR Difference Relative to 1936')
axs[1].set_xlabel('Year')
axs[1].set_ylabel('Difference in Cumulative ASFR')
axs[1].legend()
axs[1].grid(True)

# Spain
axs[2].plot(df_filtered[df_filtered['Cohort'] == 1921]['Year'][:min_length], differences['ASFR.2'][1921], label='1921 Cohort', color='blue', marker='o')
axs[2].plot(df_filtered[df_filtered['Cohort'] == 1951]['Year'][:min_length], differences['ASFR.2'][1951], label='1951 Cohort', color='green', marker='s')
axs[2].plot(df_filtered[df_filtered['Cohort'] == 1966]['Year'][:min_length], differences['ASFR.2'][1966], label='1966 Cohort', color='red', marker='^')
axs[2].set_title('Spain: Cumulative ASFR Difference Relative to 1936')
axs[2].set_xlabel('Year')
axs[2].set_ylabel('Difference in Cumulative ASFR')
axs[2].legend()
axs[2].grid(True)

# Adjust layout and show plot
plt.tight_layout()
plt.show()

# Step 9: Add the analysis in a print statement
print("\nAnalysis of Cumulative ASFR Differences:")
print("1. **USA**: The 1921 cohort shows higher cumulative fertility compared to 1936 for earlier years, but dips later.")
print("   The 1951 cohort aligns more closely with 1936 in terms of fertility timing, while the 1966 cohort shows evidence")
print("   of delayed fertility (fertility postponement), where the cumulative ASFR drops below 1936 before catching up later.")
print()
print("2. **Canada**: Similar to the USA, the 1921 cohort shows earlier fertility, while the 1966 cohort shows delayed fertility.")
print("   However, the 1951 cohort exhibits a pattern more similar to 1936 with fewer timing differences.")
print()
print("3. **Spain**: The 1921 cohort shows earlier fertility but also drops relative to 1936 after the peak. The 1966 cohort")
print("   shows fertility postponement as seen in both USA and Canada, with a more significant delay compared to 1936.")










print()
print(textwrap.dedent("""\
    2. On Blackboard, you will find an Excel file containing data on the number of deaths and exposure 
        (person-years) counts by year and sex for the US since 1933. Using Excel (or another program of 
        your choosing; if you prefer to use another program, please include documentation of your programming), 
        construct abridged period life tables (follow the US female 2019 example discussed in class) by sex 
        based on years 2020, 2019, and 1990 data. As in class, when choosing the ₙaₓ values (_n a _x), use Coale-Demeny 
        model values for very young ages and meaningful approximations (graduation, etc.) for other ages. 
        Based on your **six** constructed life tables, answer the following questions (in each case begin by 
        first stating the general expression involving the relevant life table functions (symbols) or 
        formulas):
    """))
print()
print("(a) What is the female life expectancy at birth?")
print("(b) What is the male life expectancy at birth?")
print("(c) What is life expectancy remaining for females at age 65?")
print("(d) What is life expectancy remaining for males at age 65?")
print("(e) What fraction of the female life table population survives to age 90?")
print("(f) What fraction of the male life table population survives to age 80?")
print("(g) What is the mortality rate of life table females between ages 60 and 100?")
print("(h) What is the mortality rate of life table males between ages 60 and 100?")
print("(i) What is the life table probability that a female who reaches age 70 survives to age 90?")
print("(j) What is the life table probability that a male who reaches age 70 survives to age 90?")
print("(k) What is the life table probability that a female who survives to age 1 dies between ages 1 and 5?")
print("(l) What is the number of life table males who die before their fifth birthday?")
print("(m) What is the life table probability that a newborn male dies between ages 20 and 50?")
print("(n) What is the life table probability that a female who survives to her 10th birthday dies before she reaches her 40th birthday?")
print("(o) How many person years are lived in the male life table population between ages 90 and 100?")
print("(p) On average, how many years can a life table newborn female expect to live between ages 25 and 45?")
print("(q) What is the average number of years lived by life table male newborns who die before their first birthday?")
