import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("education.csv")

print("Shape:", df.shape)
print(df.dtypes)
print("Missing values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print(df.describe())

print(df.groupby("Result")[[
    "Attendance", "Study_Hours", "Internal_Marks"
]].mean())

sns.countplot(data=df, x="Result")
plt.show()

df.hist(figsize=(8, 6))
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="Study_Hours",
                y="Internal_Marks", hue="Result")
plt.show()

sns.boxplot(data=df, x="Result", y="Attendance")
plt.show()