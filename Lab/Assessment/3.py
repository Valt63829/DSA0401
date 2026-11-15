import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("retail.csv")

print("Shape:", df.shape)
print(df.dtypes)
print("Missing values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print(df.describe())

print(df.groupby("Category")[[
    "Quantity_Sold", "Revenue"
]].sum().sort_values("Revenue", ascending=False))

sns.barplot(data=df, x="Category", y="Revenue",
            estimator=sum, errorbar=None)
plt.xticks(rotation=45)
plt.show()

df[["Price", "Quantity_Sold", "Discount", "Revenue"]].hist(
    figsize=(8, 6))
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="Quantity_Sold", y="Revenue",
                hue="Category")
plt.show()

sns.boxplot(data=df, x="Category", y="Revenue")
plt.xticks(rotation=45)
plt.show()