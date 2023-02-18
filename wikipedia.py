import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

page = requests.get(START_URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find_all('table')

tablerows = table[7].find_all('tr')

data = []

for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

star_name = []
distance = []
mass = []
radius = []

for i in range(1, len(data)):
    if len(data[i]) == 8: 
        star_name.append(data[i][0])
        distance.append(data[i][5])
        mass.append(data[i][7])
        radius.append(data[i][8])
    else:
        star_name.append(data[i][0])
        distance.append(data[i][5] if len(data[i]) > 5 else np.nan)
        mass.append(data[i][7] if len(data[i]) > 7 else np.nan)
        radius.append(data[i][8] if len(data[i]) > 8 else np.nan)

df = pd.DataFrame({'Star Name': star_name, 'Distance': distance, 'Mass': mass, 'Radius': radius})

df.to_csv('brown_dwarfs.csv', index=False)
