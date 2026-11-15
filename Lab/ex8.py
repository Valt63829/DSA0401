
import pandas as pd

sales_data = pd.DataFrame({
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop',
                'Mouse', 'Monitor', 'Keyboard', 'Mouse'],
    'quantity': [10, 50, 20, 15, 30, 12, 25, 40],
    'date': ['2026-09-15', '2026-09-18', '2026-09-20',
             '2026-09-22', '2026-09-25', '2026-09-26',
             '2026-09-28', '2026-09-30']
})

sales_data['date'] = pd.to_datetime(sales_data['date'])
monthly = sales_data[sales_data['date'].dt.month == 9]

print(monthly.groupby('product')['quantity'].sum()
      .sort_values(ascending=False).head(5))
