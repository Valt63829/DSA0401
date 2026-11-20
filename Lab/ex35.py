
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load transaction dataset
df = pd.read_csv("transactions.csv")

# Group customer transactions
customer = df.groupby("customer_id").agg(
    total_spent=("amount_spent", "sum"),
    visit_frequency=("amount_spent", "count")
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

customer["Segment"] = model.fit_predict(X)

# Display results
print("Customer Segmentation:")
print(customer)

# Visualize clusters
plt.scatter(
    customer["total_spent"],
    customer["visit_frequency"],
    c=customer["Segment"]
)

plt.xlabel("Total Amount Spent")
plt.ylabel("Visit Frequency")
plt.title("Retail Customer Segmentation")
plt.show()
