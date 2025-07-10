def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value'):
    plt.figure(figsize=(16,5))
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()


# Convert date to monthly period, then back to Timestamp for plotting
def monthlyAverage(df, city_name, pollutant):
    monthly_df = df.copy()
    monthly_df['year_month'] = monthly_df.date.dt.to_period('M').dt.to_timestamp()

    # Group by the new monthly date
    monthly_avg = monthly_df.groupby('year_month')[pollutant].mean().reset_index()

    def plot_df(x, y, title="", xlabel='Date', ylabel='Value'):
        plt.figure(figsize=(16, 5))
        plt.plot(x, y, color='tab:red')
        plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    plot_df(
        x=monthly_avg['year_month'],
        y=monthly_avg[pollutant],
        title='Monthly average concentration of {pollutant} in {city_name} from 2014 to mid-2025'.format(pollutant=pollutant, city_name=city_name),
        xlabel='Month',
        ylabel='{pollutant} Concentration'.format(pollutant=pollutant)
)


def compareMonthlyAverages(df1, city1, df2, city2, pollutant):
    # Create copies
    df1_copy = df1.copy()
    df2_copy = df2.copy()

    # Convert to monthly timestamps
    df1_copy['year_month'] = df1_copy.date.dt.to_period('M').dt.to_timestamp()
    df2_copy['year_month'] = df2_copy.date.dt.to_period('M').dt.to_timestamp()

    # Group and average
    avg1 = df1_copy.groupby('year_month')[pollutant].mean().reset_index()
    avg2 = df2_copy.groupby('year_month')[pollutant].mean().reset_index()

    # Plot
    plt.figure(figsize=(16, 5))
    plt.plot(avg1['year_month'], avg1[pollutant], label=city1, color='tab:blue')
    plt.plot(avg2['year_month'], avg2[pollutant], label=city2, color='tab:red')

    plt.title(f'Monthly average {pollutant} levels in {city1} and {city2} (2014–2025)')
    plt.xlabel('Month')
    plt.ylabel(f'{pollutant} Concentration')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def seasonalityPlot(df, city_name, pollutant):
# Create 'year' and 'month' columns
    df['year'] = df.date.dt.year
    df['month'] = df.date.dt.month
    df['month_abbr'] = df.date.dt.strftime('%b')

    # Get month order
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Aggregate: average SO2 per month per year
    monthly_avg = df.groupby(['year', 'month'])[pollutant].mean().reset_index()
    monthly_avg['month_abbr'] = monthly_avg['month'].apply(lambda x: month_order[x - 1])

    # Get unique years
    years = sorted(monthly_avg['year'].unique())

    # Random colors
    np.random.seed(100)
    mycolors = np.random.choice(list(mpl.colors.XKCD_COLORS.keys()), len(years), replace=False)

    # Plot
    plt.figure(figsize=(16, 10))

    for i, y in enumerate(years):
        year_data = monthly_avg[monthly_avg.year == y]
        plt.plot(
            year_data['month_abbr'],
            year_data[pollutant],
            color=mycolors[i],
            label=y
        )
        
        # Add year label at the end
        last_x = year_data['month_abbr'].values[-1]
        last_y = year_data[pollutant].values[-1]
        plt.text(
            x=11.2,  # right of December
            y=last_y,
            s=str(y),
            color=mycolors[i],
            fontsize=9,
            va='center'
        )

    # Final styling
    plt.xticks(ticks=range(12), labels=month_order, fontsize=12)
    plt.yticks(fontsize=12, alpha=.7)
    plt.xlabel('Month', fontsize=13)
    plt.ylabel('{pollutant} Concentration'.format(pollutant=pollutant), fontsize=13)
    plt.title('Seasonal Plot of {pollutant} Concentration in {city_name}'.format(pollutant=pollutant, city_name=city_name), fontsize=18)
    plt.grid(alpha=0.3)
    plt.xlim(-0.3, 11.5)
    plt.tight_layout()
    plt.show()

# for col in btu_df.columns:
#     if col != 'date':
#         for df in list_df_new:
#             seasonalityPlot(df, df.head(1), col)


def boxPlot(df, pollutant):
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df['year'] = df.date.dt.year
    df['month'] = df.date.dt.month
    df['month_abbr'] = df.date.dt.strftime('%b')
    fig, axes = plt.subplots(1, 2, figsize=(20,7), dpi= 80)
    sns.boxplot(x='year', y=pollutant, data=df, ax=axes[0])
    sns.boxplot(x='month_abbr', y=pollutant, data=df.loc[~df.year.isin([2013, 2026]), :], order=month_order)

    # Set Title
    axes[0].set_title('Year-wise Box Plot\n(The Trend)', fontsize=18);
    axes[1].set_title('Month-wise Box Plot\n(The Seasonality)', fontsize=18)
    plt.show()
