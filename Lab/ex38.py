
import pandas as pd

# Load temperature dataset
df = pd.read_csv("temperatures.csv")

# Calculate city statistics
result = df.groupby("city")["temperature"].agg(
    ["mean", "std", "min", "max"]
)

# Calculate temperature range
result["range"] = result["max"] - result["min"]

# Display results
print("Temperature Analysis:")
print(result)

# City with highest temperature range
highest = result["range"].idxmax()
print("\nHighest Temperature Range:", highest)

# City with most consistent temperature
consistent = result["std"].idxmin()
print("Most Consistent City:", consistent)
