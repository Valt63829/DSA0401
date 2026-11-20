
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("housing.csv")

X = df[["area", "bedrooms"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

area = float(input("Enter house area: "))
bedrooms = int(input("Enter number of bedrooms: "))

prediction = model.predict([[area, bedrooms]])

print("Predicted House Price:", prediction[0])
print("Model R2 Score:", model.score(X, y))
