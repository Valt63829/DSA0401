import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temp = [22, 24, 28, 32, 35, 34, 30, 29, 28, 27, 24, 22]
rain = [20, 15, 25, 40, 60, 120, 180, 160, 140, 100, 50, 25]

plt.plot(months, temp, marker='o', color='red')
plt.title('Monthly Temperature')
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.show()

plt.scatter(months, rain, color='blue')
plt.title('Monthly Rainfall')
plt.xlabel('Months')
plt.ylabel('Rainfall')
plt.show()