from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://coinmarketcap.com/"
request = requests.get(url)
# print(request)

soup = BeautifulSoup(request.content, "html.parser")

table = soup.find("table", class_="sc-db1da501-3 ccGPRR cmc-table")

rows = table.find_all("tr")

for row in rows[1:11]:
    table_data = row.find_all("td")
    rank = table_data[1].text
    name = table_data[2].text
    price = table_data[3].text
    hour_change = table_data[4].text
    day_change = table_data[5].text
    seven_change = table_data[6].text
    market_cap = table_data[7].text
    volume = table_data[8].text

    print(rank, name, price, hour_change, day_change, seven_change, market_cap, volume)

