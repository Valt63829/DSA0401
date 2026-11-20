
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

df = pd.read_csv("patients.csv")

X = df.drop("condition", axis=1)
y = df["condition"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

k = int(input("Enter value of K: "))

model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=k)
)

model.fit(X_train, y_train)

values = []
for col in X.columns:
    values.append(float(input("Enter " + col + ": ")))

prediction = model.predict([values])

if prediction[0] == 1:
    print("Patient has the medical condition")
else:
    print("Patient does not have the medical condition")

print("Accuracy:", accuracy_score(
    y_test, model.predict(X_test)
))
