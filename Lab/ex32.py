
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("housing.csv")

# Select feature and target
X = df[["area"]]
y = df["price"]

# Bivariate analysis
print("Correlation:", df["area"].corr(df["price"]))
print(df[["area", "price"]].describe())

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Evaluation
print("Mean Squared Error:",
      mean_squared_error(y_test, predictions))
print("R2 Score:",
      r2_score(y_test, predictions))

# Visualization
plt.scatter(X, y)
plt.plot(X, model.predict(X), color="red")
plt.xlabel("House Area")
plt.ylabel("House Price")
plt.title("House Price Prediction")
plt.show()
