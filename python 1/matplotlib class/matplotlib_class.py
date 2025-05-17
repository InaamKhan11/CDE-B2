import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime,timedelta 

start_date = datetime(2024,1,1)
end_data = datetime(2024,12,31)
num_days = (end_data - start_date).days
print(start_date,num_days)

date_list = []
for i in range(num_days):
    date_list.append(start_date.date())
    start_date += timedelta(days=1)

print(date_list)


stock_price_list = (np.random.randn(num_days)).tolist()


np.random.seed(0)
stock_price_list = (np.random.randn(num_days).cumsum()* 50).tolist()
# print(stock_price_list)


plt.figure(figsize=(15, 6))
plt.plot(date_list, stock_price_list, color='red', label='Stock Price', linewidth=2)
plt.title("Stock Price for 1 year")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.savefig("stock_price_plot.png", dpi=300)
plt.show()

