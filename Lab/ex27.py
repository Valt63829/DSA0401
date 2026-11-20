
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

df = pd.read_csv("churn.csv")

X = pd.get_dummies(df.drop("churn", axis=1), drop_first=True)
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

model.fit(X_train, y_train)

values = []
for col in X.columns:
    values.append(float(input("Enter " + col + ": ")))

prediction = model.predict([values])

if prediction[0] == 1:
    print("Customer will Churn")
else:
    print("Customer will Not Churn")

print("Accuracy:",
      accuracy_score(y_test, model.predict(X_test)))
