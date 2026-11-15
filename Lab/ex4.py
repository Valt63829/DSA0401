
import numpy as np

sales_data = np.array([10000, 12000, 15000, 18000])

total_sales = np.sum(sales_data)

q1_sales = sales_data[0]
q4_sales = sales_data[3]

percentage_increase = ((q4_sales - q1_sales) / q1_sales) * 100

print("Total Annual Sales:", total_sales)
print("Percentage Increase:", percentage_increase, "%")
