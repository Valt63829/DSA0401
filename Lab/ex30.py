
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree

df = pd.read_csv("cars.csv")

X = pd.get_dummies(df.drop("price", axis=1), drop_first=True)
y = df["price"]

model = DecisionTreeRegressor(
    max_depth=4, random_state=42
)

model.fit(X, y)

values = []

for col in X.columns:
    values.append(float(input("Enter " + col + ": ")))

car = pd.DataFrame([values], columns=X.columns)

prediction = model.predict(car)

print("Predicted Car Price:", prediction[0])

# Display decision path
decision = model.decision_path(car)

print("\nDecision Path:")

for node in decision.indices:
    if node == 0:
        continue

    feature = model.tree_.feature[node]
    threshold = model.tree_.threshold[node]

    if feature >= 0:
        print(X.columns[feature],
              "<=", threshold)

# Visualize decision tree
plt.figure(figsize=(15, 8))

plot_tree(
    model,
    feature_names=X.columns,
    filled=True
)

plt.title("CART Decision Tree")
plt.show()
