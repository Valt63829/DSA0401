import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("energy_data.csv")

# Convert date and clean data
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Consumption"] = pd.to_numeric(
    df["Consumption"], errors="coerce"
)
df.drop_duplicates(inplace=True)
df.loc[df["Consumption"] < 0, "Consumption"] = None
df["Consumption"] = df["Consumption"].fillna(
    df["Consumption"].median()
)
df.dropna(subset=["Date"], inplace=True)

# Group consumption by appliance
appliance = df.groupby("Appliance")["Consumption"].sum()
print("Appliance Consumption:\n", appliance)

# Calculate daily total consumption
daily = df.groupby("Date")["Consumption"].sum()
print("Daily Consumption:\n", daily)

# Bar chart
appliance.plot(kind="bar", title="Energy by Appliance")
plt.ylabel("Consumption (kWh)")
plt.show()

# Line chart
daily.plot(kind="line", marker="o", title="Daily Energy Usage")
plt.ylabel("Consumption (kWh)")
plt.show()