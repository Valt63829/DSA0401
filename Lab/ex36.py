
import pandas as pd
import matplotlib.pyplot as plt

# Read stock dataset
df = pd.read_csv("stock.csv")

# Closing prices
prices = df["Close"]

# Calculate statistics
mean = prices.mean()
variance = prices.var()
std = prices.std()
minimum = prices.min()
maximum = prices.max()
price_range = maximum - minimum

# Display results
print("Average Stock Price:", mean)
print("Variance:", variance)
print("Standard Deviation:", std)
print("Minimum Price:", minimum)
print("Maximum Price:", maximum)
print("Price Range:", price_range)

# Analyze variability
if std < 5:
    print("Stock price is relatively stable")
else:
    print("Stock price shows high variability")

# Plot stock prices
plt.plot(prices)
plt.xlabel("Trading Days")
plt.ylabel("Closing Price")
plt.title("Stock Price Movement")
plt.show()
