import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Import data
df = pd.read_csv('fcc-forum-pageviews.csv')
#print(df)

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Set 'date' column as the index
df.set_index('date', inplace=True)

# Calculate the lower and upper bounds for filtering
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)

# Filter the DataFrame
filtered_df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

print(filtered_df)

def draw_line_plot():
    # Load data
    df = pd.read_csv('fcc-forum-pageviews.csv')
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    
    # Filter data
    df = df[(df.index >= '2016-05-01') & (df.index <= '2019-12-31')]
    
    # Create line plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['value'], color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save the plot
    plt.savefig('line_plot.png')
    
    plt.show()

def draw_bar_plot():
    # Load data
    df = pd.read_csv('fcc-forum-pageviews.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    
    # Group data by year and month
    df_grouped = df.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Define the order of months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    # Reorder the columns based on the defined month order
    df_grouped = df_grouped.reindex(month_order, axis=1)
    # Create bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_grouped.plot(kind='bar', ax=ax)
    ax.set_title('Average Daily Page Views by Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    
    # Save the plot
    plt.savefig('bar_plot.png')
    
    plt.show()

def draw_box_plot():
    # Load data
    df = pd.read_csv('fcc-forum-pageviews.csv')
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()

    # Prepare data for box plots
    df_box_year = df.copy()
    df_box_year['year'] = df_box_year['date'].dt.year
    df_box_year['month'] = df_box_year['date'].dt.month
    df_box_year = df_box_year.rename(columns={'year': 'Year', 'month': 'Month'})

    df_box_month = df.copy()
    df_box_month['month'] = df_box_month['date'].dt.month_name()
    df_box_month = df_box_month.rename(columns={'year': 'Year', 'month': 'Month'})

    # Create box plots
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
    
    sns.boxplot(x='Year', y='value', data=df_box_year, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='Month', y='value', data=df_box_month, ax=axes[1], order=[
                 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save the plot
    plt.savefig('box_plot.png')

    plt.show()

# Uncomment the following lines to call the functions and generate the plots
#draw_line_plot()
#draw_bar_plot()
#draw_box_plot()