
import pandas as pd
import matplotlib.pyplot as plt

# Load student dataset
df = pd.read_csv("students.csv")

# Select columns
study = df["study_time"]
score = df["exam_score"]

# Calculate correlation
correlation = study.corr(score)

print("Correlation Coefficient:", correlation)

if correlation > 0:
    print("Positive Correlation")
elif correlation < 0:
    print("Negative Correlation")
else:
    print("No Correlation")

# Scatter plot
plt.scatter(study, score)
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.title("Study Time vs Exam Score")
plt.show()

# Line plot
plt.plot(study, score, marker="o")
plt.xlabel("Study Time (Hours)")
plt.ylabel("Exam Score")
plt.title("Study Time and Exam Scores")
plt.show()

# Histogram
plt.hist(score, bins=5)
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam Scores")
plt.show()
