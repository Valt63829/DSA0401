import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("learning_data.csv")

# Clean data
df.drop_duplicates(inplace=True)
df["Login_Time"] = pd.to_datetime(
    df["Login_Time"], errors="coerce"
)
df["Quiz_Score"] = df["Quiz_Score"].fillna(
    df["Quiz_Score"].median()
)
df["Completion_Percentage"] = df[
    "Completion_Percentage"
].fillna(0)

# Rank students by quiz score
df = df.sort_values("Quiz_Score", ascending=False)
df["Rank"] = df["Quiz_Score"].rank(
    ascending=False, method="dense"
)
print(df[["Student", "Quiz_Score", "Rank"]])

# Create performance categories
df["Performance"] = pd.cut(
    df["Quiz_Score"],
    bins=[-1, 40, 70, 100],
    labels=["Low", "Medium", "High"]
)
print(df[["Student", "Performance"]])

# Quiz score distribution
sns.histplot(df["Quiz_Score"], bins=10, kde=True)
plt.title("Quiz Score Distribution")
plt.show()

# Course completion
sns.barplot(data=df, x="Student", y="Completion_Percentage")
plt.title("Student Course Completion")
plt.xticks(rotation=45)
plt.show()

# Performance category
sns.countplot(data=df, x="Performance")
plt.title("Student Performance Categories")
plt.show()