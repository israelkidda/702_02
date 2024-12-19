import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.regressionplots import abline_plot

# Load the cleaned data
data_path = '/Users/israelmarykidda/Documents/MAMES/MAMES 3 Fall 2024/DCP 702 Methods of Demographic Analysis/final paper main/final final dec 19/final data/clean_data.csv'
data = pd.read_csv(data_path)

# Define a function to run ITSA and plot with improvements
def run_itsa_and_plot(data, category, sex, intervention_year=1995, annotate_p_values=False):
    subset = data[(data['Category'] == category) & (data['Sex'] == sex)]
    subset['time_post'] = (subset['Time'] - intervention_year).clip(lower=0)
    subset['intervention'] = (subset['Time'] >= intervention_year).astype(int)
    
    # Fit the ITSA model
    X = sm.add_constant(subset[['Time', 'intervention', 'time_post']])
    model = sm.OLS(subset['Value'], X).fit()
    
    # Predictions
    subset['predicted'] = model.predict(X)
    
    # Plot observed vs. predicted
    plt.figure(figsize=(10, 6))
    plt.plot(subset['Time'], subset['Value'], label='Observed', marker='o')
    plt.plot(subset['Time'], subset['predicted'], label='Predicted', linestyle='--')
    
    # Highlight intervention
    plt.axvline(x=intervention_year, color='red', linestyle=':', label=f'Intervention ({intervention_year})')
    
    # Annotate p-values if enabled
    if annotate_p_values:
        plt.text(intervention_year + 0.5, max(subset['Value']) - 1,
                 f"Level p = {model.pvalues['intervention']:.3f}\nSlope p = {model.pvalues['time_post']:.3f}",
                 color='blue')
    
    # Labeling
    plt.title(f"{category} Analysis - {sex}")
    plt.xlabel("Year")
    plt.ylabel(f"{category} Rate")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

# Run and visualize for each category and sex
for category in ['IMR', 'U5MR']:
    for sex in ['Male', 'Female', 'Both sexes']:
        run_itsa_and_plot(data, category, sex, annotate_p_values=True)

























import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Example function to generate enhanced graphs

def plot_with_enhancements(data, model, intervention_year, outcome_label, title):
    """
    Generate enhanced graphs with confidence intervals, color-coded slopes,
    and additional bar charts for level and slope changes.
    """
    # Extract data
    pre_data = data[data['Time'] < intervention_year]
    post_data = data[data['Time'] >= intervention_year]

    # Confidence intervals
    X = sm.add_constant(data[['Time', 'intervention', 'time_post']])
    predictions = model.get_prediction(X)
    prediction_summary = predictions.summary_frame()

    # Plot observed and predicted
    plt.figure(figsize=(10, 6))
    plt.plot(data['Time'], data['Value'], label="Observed", marker="o", color="blue")
    plt.plot(data['Time'], prediction_summary['mean'], label="Predicted", linestyle="--", color="orange")

    # Add confidence intervals
    plt.fill_between(
        data['Time'],
        prediction_summary['mean_ci_lower'],
        prediction_summary['mean_ci_upper'],
        color="orange",
        alpha=0.2,
        label="95% CI",
    )

    # Color-coded slopes
    plt.plot(pre_data['Time'], prediction_summary['mean'][:len(pre_data)], color="green", label="Pre-Intervention")
    plt.plot(post_data['Time'], prediction_summary['mean'][len(pre_data):], color="red", label="Post-Intervention")

    # Annotate slopes and p-values
    slope_pre = model.params['Time']
    slope_post = model.params['Time'] + model.params['time_post']
    p_level = model.pvalues['intervention']
    p_slope = model.pvalues['time_post']

    plt.text(
        intervention_year + 0.5,
        prediction_summary['mean'].max(),
        f"Level p = {p_level:.3f}\nSlope p = {p_slope:.3f}",
        color="blue",
    )

    # Add intervention line
    plt.axvline(intervention_year, color="red", linestyle="--", label="Intervention")

    # Labels and legend
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(outcome_label)
    plt.legend()
    plt.grid()
    plt.show()

    # Bar chart for level and slope changes
    plt.figure(figsize=(6, 4))
    changes = [
        model.params['intervention'],
        model.params['time_post'],
    ]
    p_values = [
        model.pvalues['intervention'],
        model.pvalues['time_post'],
    ]
    labels = ["Level Change", "Slope Change"]
    colors = ["green" if p < 0.05 else "grey" for p in p_values]

    plt.bar(labels, changes, color=colors, alpha=0.7)
    for i, (change, p) in enumerate(zip(changes, p_values)):
        plt.text(i, change, f"p = {p:.3f}", ha="center", va="bottom" if change < 0 else "top")

    plt.title("Level and Slope Changes")
    plt.ylabel("Change Magnitude")
    plt.grid(axis="y")
    plt.show()

# Example use case
# Assuming data, model, and intervention_year are already defined for ITSA analysis
# plot_with_enhancements(data, model, 1995, "IMR Rate", "IMR Analysis - Enhanced")
