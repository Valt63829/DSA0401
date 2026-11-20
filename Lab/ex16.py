import pandas as pd
import re
from collections import Counter

data = {'Reviews': [
    'Product quality is good',
    'Product is very useful',
    'Good product and good quality',
    'Product quality is excellent'
]}

df = pd.DataFrame(data)

text = ' '.join(df['Reviews']).lower()
text = re.sub(r'[^\w\s]', '', text)

frequency = Counter(text.split())

for word, count in frequency.items():
    print(word, ":", count)