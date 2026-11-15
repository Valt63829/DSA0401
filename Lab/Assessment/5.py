import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("agriculture.csv")

print("Shape:", df.shape)
print(df.dtypes)
print("Missing values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print(df.describe())

print(df.groupby("Soil_Type")["Crop_Yield_kg"].mean())

sns.barplot(data=df, x="Soil_Type", y="Crop_Yield_kg",
            errorbar=None)
plt.show()

df[["Rainfall_mm", "Temperature", "Fertilizer_kg",
    "Crop_Yield_kg"]].hist(figsize=(8, 6))
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="Rainfall_mm", y="Crop_Yield_kg",
                hue="Soil_Type")
plt.show()

sns.boxplot(data=df, x="Soil_Type", y="Crop_Yield_kg")
plt.show()