"""
Note:

1. find = fetch first element
2. find_all = fetch all elements

3. .text.strip() remove all spaces and new lines

"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"
request = requests.get(url)
print(request)

soup = BeautifulSoup(request.content, "html.parser")

title = soup.find("h2", class_="title is-5").text.strip()
sub_title = soup.find("h3", class_="subtitle is-6 company").text.strip()
location = soup.find("p", class_="location").text.strip()
date = soup.find("p", class_="is-small has-text-grey").text.strip()



divs = soup.find_all("div", class_="column is-half")

all_data = []

for div in divs:
    data = []
    title = div.find("h2", class_="title is-5").text
    sub_title = div.find("h3", class_="subtitle is-6 company").text.strip() 
    location = div.find("p", class_="location").text.strip()
    date = div.find("p", class_="is-small has-text-grey").text.strip()
    date = [title, sub_title, location, date]
    all_data.append(date) 

print(all_data)


