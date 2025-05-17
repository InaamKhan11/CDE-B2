from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

path = r'D:\programming\CDE-B2\python 1\web scraping\chrome_driver\chromedriver-win64\chromedriver.exe'
# this path is for chromedriver.exe

ser = Service(path)

driver = webdriver.Chrome(path)

driver.get("https://www.psx.com.pk/market-summary/")
time.sleep(5)

# Scroll down to load more data
table = driver.find_element(By.ID , "marketmainboard")

rows = table.find_elements(By.TAG_NAME, 'tr')

data = []

for row in rows:
    tds = row.find_elements(By.TAG_NAME, 'td')
    if tds:
        first_cell = tds[0].text.strip()
        # Skip if it's a repeated header row
        if first_cell.upper() == "SCRIP":
            continue
        row_data = [td.text.strip() for td in tds]
        data.append(row_data)

# Write to CSV
filename = "psx_clean_data.csv"
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write actual header once
    writer.writerow(["SCRIP", "LDCP", "OPEN", "HIGH", "LOW", "CURRENT", "CHANGE", "VOLUME"])
    writer.writerows(data)

print(f"Clean data saved to {filename}")

driver.quit()
