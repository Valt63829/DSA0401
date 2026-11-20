import numpy as np

# Columns: Bedrooms, Square Footage, Sale Price
house_data = np.array([
    [3, 1500, 200000],
    [5, 2500, 350000],
    [4, 1800, 250000],
    [6, 3000, 450000],
    [5, 2200, 400000]
])

# Select houses with more than 4 bedrooms
selected_houses = house_data[house_data[:, 0] > 4]

# Calculate average sale price (column index 2)
average_price = np.mean(selected_houses[:, 2])

print("Average sale price:", average_price)