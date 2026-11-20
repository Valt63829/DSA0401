import numpy as np

# Marks of 4 students in the order: Math, Science, English, History
student_scores = np.array([
    [85, 90, 78, 88],
    [92, 85, 80, 75],
    [76, 95, 85, 82],
    [88, 80, 90, 86]
])

# Calculate average score for each subject
averages = np.mean(student_scores, axis=0)

# Subject names
subjects = ["Math", "Science", "English", "History"]

# Display average scores
for subject, avg in zip(subjects, averages):
    print(f"Average score in {subject}: {avg:.2f}")

# Find the subject with the highest average
highest_index = np.argmax(averages)

print(f"\nSubject with highest average: {subjects[highest_index]}")
print(f"Highest average score: {averages[highest_index]:.2f}")