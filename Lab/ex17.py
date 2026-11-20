import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

df = pd.read_csv('data.csv')

text = ' '.join(df['feedback'].dropna()).lower()
text = re.sub(r'[^a-z\s]', '', text)

words = [w for w in text.split()
         if w not in ENGLISH_STOP_WORDS]

frequency = Counter(words)

n = int(input("Enter N: "))
top = frequency.most_common(n)

print(top)

if top:
    w, c = zip(*top)
    plt.bar(w, c)
    plt.title('Top Frequent Words')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()