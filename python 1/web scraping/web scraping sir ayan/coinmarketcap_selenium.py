from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv

path = r'D:\programming\CDE-B2\python 1\web scraping\chrome_driver\chromedriver-win64\chromedriver.exe'

# Starting the Chrome driver service
ser = Service(path)
# ser.start()
# Create a new instance of the Chrome driver
driver = webdriver.Chrome(path)

driver.get("https://coinmarketcap.com/")

for i in range(15):
    driver.execute_script("window.scrollBy(0, 800);") 
    time.sleep(2) 

table = driver.find_element(By.CLASS_NAME, 'cmc-table')

rows = table.find_elements(By.TAG_NAME, 'tr')
print("Number of rows in the table:", len(rows))


# Loop through the rows and print the text of each cell
with open('coinmarketcap_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Rank', 'Name', 'Price', '1h %', '24h %', '7d %', 'Market Cap', 'Volume'])
    for row in rows[1:]:
        table_data = row.find_elements(By.TAG_NAME,'td')
        if len(table_data) < 9:
            continue  # Skip incomplete rows
        rank = table_data[1].text
        name = table_data[2].text
        price = table_data[3].text
        hour_change = table_data[4].text
        day_change = table_data[5].text
        seven_days_change = table_data[6].text
        market_cap = table_data[7].text
        volume = table_data[8].text
        writer.writerow([rank, name, price, hour_change, day_change, seven_days_change, market_cap, volume])
        print(f"{rank} | {name} | {price} | {hour_change} | {day_change} | {seven_days_change} | {market_cap} | {volume}")

driver.quit()


