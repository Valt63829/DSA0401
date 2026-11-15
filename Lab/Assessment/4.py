import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("banking.csv")

print("Shape:", df.shape)
print(df.dtypes)
print("Missing values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print(df.describe())

print(df.groupby("Loan_Status")[[
    "Income", "Credit_Score", "Loan_Amount"
]].mean())

sns.countplot(data=df, x="Loan_Status")
plt.show()

df[["Income", "Credit_Score", "Loan_Amount"]].hist(
    figsize=(8, 6))
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="Income", y="Credit_Score",
                hue="Loan_Status")
plt.show()

sns.boxplot(data=df, x="Loan_Status", y="Credit_Score")
plt.show()