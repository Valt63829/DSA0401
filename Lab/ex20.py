import pandas as pd

df = pd.read_csv('customer_data.csv')

low = df['Total Spending'].quantile(0.33)
high = df['Total Spending'].quantile(0.67)

df['Segment'] = pd.cut(
    df['Total Spending'],
    bins=[-float('inf'), low, high, float('inf')],
    labels=['Low Spenders', 'Medium Spenders',
            'High Spenders'],
    include_lowest=True
)

print(df)

print("\nAverage Age:")
print(df.groupby('Segment', observed=False)['Age'].mean())