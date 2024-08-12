import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

all_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Step 1: Import the data
# Read the CSV file and parse the dates in the 'date' column.
# Also set 'date' as the index of the DataFrame to help with time series analysis.
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Step 2: Clean the data
# Filter out the top and bottom 2.5% of the data to remove outliers.
# This helps focus on the main trend in the data without being skewed by extreme values.
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Step 3: Draw line plot
    # Create a figure and axis for the plot
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot the data on the DataFrame
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    # Set title and labels of the plot
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Step 4: Copy and modify data for monthly bar plot
    # Group data by year and month to get the average page views average per month
    # To get it, create new columns for the month and year based on index
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Then group year and month to get the average
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Step 5: Draw bar plot
    # Create the fig and axis
    fig, ax = plt.subplots(figsize=(10, 5))

    # Create the bar chart
    df_bar.plot(kind='bar', ax=ax)

    # Set title, labels, and legends
    ax.set_title('Average Daily Page Views per Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Step 6: Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    # Step 7: Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    # Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot (Season)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=all_months)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
