
import numpy as np

fuel_efficiency = np.array([25, 30, 35, 40])

average_efficiency = np.mean(fuel_efficiency)

model1 = fuel_efficiency[0]
model2 = fuel_efficiency[3]

percentage_improvement = ((model2 - model1) / model1) * 100

print("Average Fuel Efficiency:", average_efficiency, "mpg")
print("Percentage Improvement:", percentage_improvement, "%")
