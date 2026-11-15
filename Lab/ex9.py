
import pandas as pd

property_data = pd.DataFrame({
    'id': [101, 102, 103, 104, 105],
    'location': ['Chennai', 'Ongole', 'Chennai', 'Hyderabad', 'Ongole'],
    'bedrooms': [3, 5, 4, 6, 2],
    'area': [1200, 2500, 1800, 3000, 1000],
    'price': [5000000, 8000000, 6500000, 12000000, 3500000]
})

print("Average Price:\n", property_data.groupby('location')['price'].mean())
print("Properties with >4 Bedrooms:", (property_data['bedrooms'] > 4).sum())
print("Largest Property:\n", property_data.loc[property_data['area'].idxmax()])
