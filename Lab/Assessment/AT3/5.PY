import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("transport_data.csv")

# Clean data
df["Route"] = pd.to_numeric(df["Route"], errors="coerce")
df["Passenger_Count"] = pd.to_numeric(
    df["Passenger_Count"], errors="coerce"
)
df.drop_duplicates(inplace=True)
df = df[df["Route"] > 0]
df["Passenger_Count"] = df["Passenger_Count"].fillna(
    df["Passenger_Count"].median()
)

# Analyze passengers by route
routes = df.groupby("Route")["Passenger_Count"].sum()
print("Passengers by Route:\n", routes.sort_values(ascending=False))

# Analyze passengers by stop
stops = df.groupby("Stop")["Passenger_Count"].sum()
print("Passengers by Stop:\n", stops.sort_values(ascending=False))

# Analyze passengers by time slot
hours = df.groupby("Time_Slot")["Passenger_Count"].sum()
print("Passengers by Time Slot:\n", hours)

# Busiest routes
routes.nlargest(5).plot(kind="bar", title="Top 5 Busiest Routes")
plt.ylabel("Passenger Count")
plt.show()

# Peak travel hours
hours.plot(kind="line", marker="o", title="Passenger Flow by Time Slot")
plt.ylabel("Passenger Count")
plt.show()

# Passenger flow heatmap
pivot = df.pivot_table(
    index="Route",
    columns="Time_Slot",
    values="Passenger_Count",
    aggfunc="sum",
    fill_value=0
)
sns.heatmap(pivot, cmap="YlGnBu")
plt.title("Passenger Flow by Route and Time")
plt.show()