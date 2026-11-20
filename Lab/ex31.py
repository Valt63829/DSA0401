
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load customer dataset
df = pd.read_csv("customer_data.csv")

# Select numerical features
X = df.select_dtypes(include="number")
X = X.drop(columns=["customer_id"], errors="ignore")

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means
k = 3
model = KMeans(n_clusters=k, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(X_scaled)

# Display customer groups
print("Customer Segmentation:")
print(df[["Cluster"]])

print("\nCluster Summary:")
print(df.groupby("Cluster")[X.columns].mean())

# Visualize clusters
plt.scatter(X.iloc[:, 0], X.iloc[:, 1],
            c=df["Cluster"])
plt.xlabel(X.columns[0])
plt.ylabel(X.columns[1])
plt.title("Customer Segmentation")
plt.show()
