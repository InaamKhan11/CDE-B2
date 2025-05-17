import matplotlib.pyplot as plt


year = [2020, 2021, 2022, 2023, 2024, 2025]
sales = [100, 130, 199, 270, 420, 300]

plt.bar(year, sales)
plt.plot(year, sales, color='red', marker='o', label='Sales Trend')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Over Years')
plt.legend()
plt.show()
