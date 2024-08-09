import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the dataset into a DataFrame
df = pd.read_csv('medical_examination.csv')

# 2. Add an 'overweight' column
# Calculate BMI: weight (kg) / height (m)^2
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
# A BMI value over 25 is considered overweight
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3. Normalize the data
# Cholesterol and Glucose: 0 is good, 1 is bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Function to draw the categorical plot
def draw_cat_plot():
    # 5. Melt the DataFrame to convert it into a long format suitable for categorical plotting
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group by 'cardio', 'variable', and 'value' to count the occurrences
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).size()

    # 7. Create the categorical plot using seaborn's catplot
    g = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count', height=5, aspect=1.2)

    # Explicitly set ylabel to "total"
    g.set_axis_labels("variable", "total")

    # Extract the figure from the FacetGrid object
    fig = g.fig

    # 8. Save the plot as 'catplot.png'
    fig.savefig('catplot.png')
    return fig

# 10. Function to draw the heatmap
def draw_heat_map():
    # 11. Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
                 (df['height'] >= df['height'].quantile(0.025)) & 
                 (df['height'] <= df['height'].quantile(0.975)) & 
                 (df['weight'] >= df['weight'].quantile(0.025)) & 
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # Drop the 'BMI' column to match expected test results
    df_heat = df_heat.drop(columns=['BMI'])

    # 12. Calculate the correlation matrix
    corr = df_heat.corr()

    # 13. Generate a mask for the upper triangle of the matrix
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # 15. Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', ax=ax)

    # 16. Save the heatmap as 'heatmap.png'
    fig.savefig('heatmap.png')
    return fig

# These functions can now be called to generate the desired visualizations.
