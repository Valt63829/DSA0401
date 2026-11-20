
import pandas as pd
import matplotlib.pyplot as plt

# Create soccer player dataset
data = {
    "Name": ["Ali", "John", "Ravi", "David", "Omar",
             "Sam", "Leo", "Noah"],
    "Age": [24, 29, 22, 31, 27, 25, 30, 21],
    "Position": ["Forward", "Midfielder", "Defender",
                 "Forward", "Goalkeeper", "Midfielder",
                 "Defender", "Forward"],
    "Goals": [18, 8, 2, 15, 0, 6, 3, 12],
    "Salary": [5000, 4500, 3000, 6000, 3500,
               4000, 4200, 3800]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save dataset to CSV
df.to_csv("soccer_players.csv", index=False)

print("Soccer Dataset:")
print(df)

# Top 5 players by goals
print("\nTop 5 Players by Goals:")
print(df.nlargest(5, "Goals")[["Name", "Goals"]])

# Top 5 players by salary
print("\nTop 5 Players by Salary:")
print(df.nlargest(5, "Salary")[["Name", "Salary"]])

# Calculate average age
average_age = df["Age"].mean()

print("\nAverage Age:", average_age)

# Players above average age
print("\nPlayers Above Average Age:")
print(df[df["Age"] > average_age]["Name"])

# Visualize players by position
df["Position"].value_counts().plot(kind="bar")

plt.xlabel("Player Position")
plt.ylabel("Number of Players")
plt.title("Players Distribution by Position")
plt.show()
