import pandas as pd

df = pd.read_csv('sales_data.csv')

df['Total Sales'] = df['Quantity Sold'] * df['Unit Price']
df['Profit'] = df['Total Sales'] * 0.20

result = df.groupby('Product').agg(
    Total_Sales=('Total Sales', 'sum'),
    Profit=('Profit', 'sum')
)

print(result.sort_values('Profit', ascending=False).head(5))