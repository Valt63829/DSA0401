
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import (
    accuracy_score, precision_score,
    recall_score, f1_score
)

# Load dataset
df = pd.read_csv("treatment.csv")

# Features and target
X = pd.get_dummies(df.drop("outcome", axis=1),
                   drop_first=True)
y = df["outcome"]

# Convert outcomes into numbers
y = y.map({"Bad": 0, "Good": 1})

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42,
    stratify=y
)

# Train KNN model
model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions))
print("Recall:", recall_score(y_test, predictions))
print("F1 Score:", f1_score(y_test, predictions))

# Display predictions
print("\nPredictions:")
for p in predictions:
    print("Good" if p == 1 else "Bad")
