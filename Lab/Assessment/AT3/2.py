import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("loan_data.csv")

cols = ["Income", "Loan_Amount", "Credit_Score",
        "Approval_Status", "Gender", "Employment_Type"]
df = df[cols].drop_duplicates().copy()

df["Income"] = df["Income"].fillna(df["Income"].median())
df["Loan_Amount"] = df["Loan_Amount"].fillna(
    df["Loan_Amount"].median()
)
df["Credit_Score"] = df["Credit_Score"].fillna(
    df["Credit_Score"].median()
)

df = df[(df["Income"] >= 0) & (df["Loan_Amount"] > 0)]

df = pd.get_dummies(df, columns=["Gender", "Employment_Type"],
                    dtype=int)
scaler = MinMaxScaler()
df["Loan_Amount"] = scaler.fit_transform(df[["Loan_Amount"]])

# Compare loan approval status
sns.boxplot(data=df, x="Approval_Status", y="Income")
plt.title("Income vs Loan Approval")
plt.show()

sns.boxplot(data=df, x="Approval_Status", y="Credit_Score")
plt.title("Credit Score vs Loan Approval")
plt.show()

sns.boxplot(data=df, x="Approval_Status", y="Loan_Amount")
plt.title("Loan Amount vs Loan Approval")
plt.show()