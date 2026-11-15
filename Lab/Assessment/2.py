import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("healthcare.csv")

print("Shape:", df.shape)
print(df.dtypes)
print("Missing values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print(df.describe())

print(df.groupby("Disease_Status")[[
    "Age", "Sugar_Level", "BP", "BMI"
]].mean())

sns.countplot(data=df, x="Disease_Status")
plt.show()

df[["Age", "Sugar_Level", "BP", "BMI"]].hist(figsize=(8, 6))
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="Age", y="Sugar_Level",
                hue="Disease_Status")
plt.show()

sns.boxplot(data=df, x="Disease_Status", y="BMI")
plt.show()  