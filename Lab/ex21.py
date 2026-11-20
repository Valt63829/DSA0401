
import numpy as np
from scipy import stats

data = np.loadtxt("rare_elements.csv", delimiter=",", skiprows=1)

n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (e.g. 95): ")) / 100
precision = float(input("Enter desired precision: "))

sample = np.random.choice(data, n, replace=False)

mean = np.mean(sample)
std = np.std(sample, ddof=1)

z = stats.norm.ppf(1 - (1 - confidence) / 2)
margin = z * std / np.sqrt(n)

print("Sample Mean:", mean)
print("Confidence Interval:", mean - margin, "to", mean + margin)
print("Margin of Error:", margin)

if margin <= precision:
    print("Desired precision achieved")
else:
    print("Desired precision not achieved")
