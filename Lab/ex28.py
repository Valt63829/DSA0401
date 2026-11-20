
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("customers.csv")

X = df[["annual_income", "spending_score"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

k = int(input("Enter number of clusters: "))

model = KMeans(n_clusters=k, random_state=42, n_init=10)
model.fit(X_scaled)

income = float(input("Enter annual income: "))
score = float(input("Enter spending score: "))

customer = scaler.transform([[income, score]])

cluster = model.predict(customer)

print("Customer belongs to Cluster:", cluster[0] + 1)

plt.scatter(X["annual_income"], X["spending_score"],
            c=model.labels_)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()
