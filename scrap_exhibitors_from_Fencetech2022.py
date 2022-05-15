#target website https://www.expocad.com/host/fx/afa/ft2022/exfx.html, but I found the exhibitor info is stored in 'https://www.expocad.com/host/fx/afa/ft2022/ft2022.xml'

import requests
from bs4 import BeautifulSoup
import pandas as pd

res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'xml')

Booths = []
Exhibitors = []
datas = soup.findAll('S')
for data in datas:
    infos = data.findAll('T')
    if len(infos) > 1:
        booth = infos[0].get('v')
        exhibitor = ""
        for info in infos[1:]:
            exhibitor += info.get('v') + ' '
        Booths.append(booth)
        Exhibitors.append(exhibitor)
df = pd.DataFrame({'Booth' : Booths,'Exhibitor':Exhibitors})
df.to_csv('exhibitor_list_from_Fencetech2022.csv')
