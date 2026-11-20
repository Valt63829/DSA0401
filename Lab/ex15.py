import pandas as pd

data = {'Likes': [100, 200, 100, 300, 200,
                  100, 400, 300, 200, 100]}

df = pd.DataFrame(data)

frequency = df['Likes'].value_counts().sort_index()

print(frequency)