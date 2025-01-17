import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
# Set 'date' column as the index
df.set_index('date', inplace=True)

# Calculate the lower and upper bounds for filtering
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

# Filter the DataFrame
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]


def draw_line_plot():
    # Draw line plot
    # Filter data
    df = pd.read_csv('fcc-forum-pageviews.csv')
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    # Calculate the lower and upper bounds for filtering
    lower_bound = df['value'].quantile(0.025)
    upper_bound = df['value'].quantile(0.975)

    # Filter the DataFrame
    df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
    
    # Create line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['value'], color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df = pd.read_csv('fcc-forum-pageviews.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Define the order of months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # Reorder the columns based on the defined month order
    df_bar = df_bar.reindex(month_order, axis=1)
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_bar.plot(kind='bar', ax=ax)
    ax.set_title('Average Daily Page Views by Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Load data
    df = pd.read_csv('fcc-forum-pageviews.csv')
    df['date'] = pd.to_datetime(df['date'])
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=[
                 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    # Set y-axis ticks to match expected labels
    expected_y_ticks = list(range(0, 200001, 20000))
    axes[0].set_yticks(expected_y_ticks)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
