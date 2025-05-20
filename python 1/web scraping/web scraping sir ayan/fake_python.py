from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"
request = requests.get(url)

soup = BeautifulSoup(request.text, 'html.parser')

jobs = soup.find('div', class_="columns is-multiline")

dtl = jobs.find_all('div', class_="column is-half")


job_list = []
for job in dtl:
    title = job.find('h2', class_="title is-5").text.strip()
    subtitle = job.find('h3', class_="subtitle is-6 company").text.strip()
    location = job.find('p', class_='location').text.strip()
    date = job.find('time')['datetime']
    job_list.append({'Title': title, 'Subtitle': subtitle, 'Location': location, 'Date': date})



df = pd.DataFrame(job_list)
df.index += 1
df.to_csv('fake_jobs.csv', index=True, encoding='utf-8')
print("Data has been written to fake_jobs.csv")