
import pandas as pd
import csv

from bs4 import BeautifulSoup
import requests
url = BeautifulSoup(
    'https://www.worldometers.info/coronavirus/', 'html.parser')
soup = requests.get(url)
print(soup)
# print(soup.text)
code = BeautifulSoup(soup.text, "lxml")
# print(code)
table_code = code.table
# print(table_code)
tags = table_code.find_all('tr')
# print(tags)
raw_data = []
for tag in tags:
    x = tag.text
    raw_data.append(x.split('\n')[1:-1])
    raw_data.remove()
print(raw_data)

# print(tag.text)
with open('covid.csv', 'w')as file:
    x = csv.writer(file)
    for i in raw_data:
        x.writerow(i)

# df = pd.read_csv('covid.csv', encoding='ISO-8859-1')
# print(df)
