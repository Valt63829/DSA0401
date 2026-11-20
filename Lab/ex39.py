
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load transaction dataset
df = pd.read_csv("transactions.csv")

# Group customer data
customer = df.groupby("customer_id").agg(
    spending=("amount_spent", "sum"),
    items=("items_purchased", "sum")
)

# Standardize data
scaler = StandardScaler()
X = scaler.fit_transform(customer)

# Apply K-Means
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

customer["Cluster"] = model.fit_predict(X)

# Display clusters
print("Customer Groups:")
print(customer)

# Visualize clusters
plt.scatter(
    customer["spending"],
    customer["items"],
    c=customer["Cluster"]
)

plt.xlabel("Total Spending")
plt.ylabel("Items Purchased")
plt.title("Customer Spending Clusters")
plt.show()
