
import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("customer_reviews.csv")

ratings = df["rating"].dropna()

n = len(ratings)
mean = ratings.mean()
std = ratings.std()

t = stats.t.ppf(0.975, n - 1)
margin = t * std / np.sqrt(n)

print("Average Rating:", mean)
print("95% Confidence Interval:")
print("Lower Limit:", mean - margin)
print("Upper Limit:", mean + margin)

if mean >= 4:
    print("Customer Satisfaction: High")
elif mean >= 3:
    print("Customer Satisfaction: Medium")
else:
    print("Customer Satisfaction: Low")
