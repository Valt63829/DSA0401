import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("food_delivery.csv")

# Clean data
df.drop_duplicates(inplace=True)
df["Delivery_Time"] = df["Delivery_Time"].fillna(
    df["Delivery_Time"].median()
)
df = df[df["Price"] > 0]

# Filter delayed orders
delayed = df[df["Delivery_Time"] > 30]
print("Delayed Orders:\n", delayed)

# Top restaurants
top = df["Restaurant"].value_counts().head(5)
top.plot(kind="bar", title="Top Restaurants")
plt.show()

# Customer ratings
sns.histplot(df["Rating"].dropna(), bins=5)
plt.title("Customer Ratings")
plt.show()

# Delivery time distribution
sns.histplot(df["Delivery_Time"], kde=True)
plt.title("Delivery Time Distribution")
plt.show()