import pandas as pd

data = {'Age': [22, 25, 22, 30, 25, 35, 30, 22, 40, 25]}

df = pd.DataFrame(data)

frequency = df['Age'].value_counts().sort_index()

print(frequency)