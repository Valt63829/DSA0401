import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [100, 150, 180, 130, 220, 250]

plt.plot(months, sales, marker='o')
plt.title('Line Plot')
plt.show()

plt.scatter(months, sales, color='red')
plt.title('Scatter Plot')
plt.show()

plt.bar(months, sales, color='orange')
plt.title('Bar Plot')
plt.show()