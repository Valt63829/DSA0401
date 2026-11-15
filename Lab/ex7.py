
import pandas as pd

order_data = pd.DataFrame({
    'customer_id': [101, 102, 101, 103, 102],
    'order_date': ['2026-01-05', '2026-01-10', '2026-02-15',
                   '2026-02-20', '2026-03-01'],
    'product_name': ['Laptop', 'Mouse', 'Mouse', 'Keyboard', 'Laptop'],
    'order_quantity': [1, 2, 3, 1, 2]
})

order_data['order_date'] = pd.to_datetime(order_data['order_date'])

print("Orders per Customer:\n", order_data.groupby('customer_id').size())
print("Average Quantity:\n", order_data.groupby('product_name')['order_quantity'].mean())
print("Earliest Date:", order_data['order_date'].min().date())
print("Latest Date:", order_data['order_date'].max().date())
