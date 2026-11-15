import numpy as np

# 3x3 matrix: Product, with 3 sales prices each
sales_data = np.array([
    [100, 150, 200],
    [250, 300, 350],
    [400, 450, 500]
])

# Calculate average price
average_price = np.mean(sales_data)

print("Average price of all products:", average_price)