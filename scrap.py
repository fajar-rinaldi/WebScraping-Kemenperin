import requests
from bs4 import BeautifulSoup
import pandas as pd

name_list = []
for i in range(1,2):
    url = f'https://kemenperin.go.id/direktori-perusahaan?what=Medan&prov=0{i}'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    rows =soup.find('table', {'id': 'newspaper-a'}).find('tbody').find_all('tr')

    

    for row in rows:
        dic = {}
        dic['Perusahaan'] = row.find_all('td')
        dic['KBLI'] = row.find_all('td')

        name_list.append(dic)

    df = pd.DataFrame(name_list)
    df.to_csv('Medan.csv', index=False)

  