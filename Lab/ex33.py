
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load car dataset
df = pd.read_csv("car_prices.csv")

# Select features
X = pd.get_dummies(
    df.drop("price", axis=1),
    drop_first=True
)
y = df["price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict prices
predictions = model.predict(X_test)

# Evaluate model
print("Mean Squared Error:",
      mean_squared_error(y_test, predictions))
print("R2 Score:",
      r2_score(y_test, predictions))

# Important features
importance = pd.Series(
    model.coef_, index=X.columns
)

print("\nImportant Factors:")
print(importance.sort_values(
    key=abs, ascending=False
))
