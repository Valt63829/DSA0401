
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (
    accuracy_score, precision_score,
    recall_score, f1_score
)

df = pd.read_csv("dataset.csv")

features = input(
    "Enter feature names separated by commas: "
).split(",")

features = [x.strip() for x in features]

target = input("Enter target variable name: ")

X = pd.get_dummies(df[features], drop_first=True)
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

print("Precision:",
      precision_score(y_test, predictions,
                      average="weighted", zero_division=0))

print("Recall:",
      recall_score(y_test, predictions,
                   average="weighted", zero_division=0))

print("F1 Score:",
      f1_score(y_test, predictions,
               average="weighted", zero_division=0))
