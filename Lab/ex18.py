import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

data = {
    'Age': [23,25,28,30,32,35,38,40,42,
            45,47,50,52,55,58,60,62,65],
    'Fat': [18,20,22,21,24,25,27,28,26,
            30,31,33,32,35,36,38,37,40]
}

df = pd.DataFrame(data)

print("Mean:\n", df.mean())
print("Median:\n", df.median())
print("Standard Deviation:\n", df.std())

df.boxplot()
plt.title('Age and Body Fat Boxplot')
plt.show()

plt.scatter(df['Age'], df['Fat'])
plt.xlabel('Age')
plt.ylabel('Body Fat')
plt.title('Age vs Body Fat')
plt.show()

stats.probplot(df['Age'], dist='norm', plot=plt)
plt.title('Q-Q Plot of Age')
plt.show()

stats.probplot(df['Fat'], dist='norm', plot=plt)
plt.title('Q-Q Plot of Fat')
plt.show()