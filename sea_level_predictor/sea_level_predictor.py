import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_ext = pd.Series(range(1880, 2051))
    plt.plot(years_ext, res_full.intercept + res_full.slope * years_ext, 'r', label='Fit 1880-2050')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000 = pd.Series(range(2000, 2051))
    plt.plot(years_2000, res_2000.intercept + res_2000.slope * years_2000, 'g', label='Fit 2000-2050')



    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()