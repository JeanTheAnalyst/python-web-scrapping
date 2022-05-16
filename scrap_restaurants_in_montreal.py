
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from fake_useragent import UserAgent



Name = []
Street_address = []
Locality = []
Region = []
Postal_code = []
Phone_number = []

headers = {'user-agent':UserAgent().random}


for i in range(1,185):
    url =f'https://www.yellowpages.ca/search/si/{i}/restaurants/Montreal+QC'
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    datas = soup.findAll('div',class_='listing_right_section')
    for data in datas:
        name = data.find('a',class_='listing__name--link').text
        addresses = data.findAll('span',class_='jsMapBubbleAddress')
        street_address = addresses[0].text if len(addresses)>0 else 'N/A'
        locality = addresses[1].text if len(addresses)>1 else 'N/A'
        region = addresses[2].text if len(addresses)>2 else 'N/A'
        postcode = addresses[3].text if len(addresses)>3 else 'N/A'
        phone_number = data.find('a', class_='mlr__item__cta').get('data-phone')
        
        
        Name.append(name) 

        Street_address.append(street_address)
        Locality.append(locality)
        Region.append(region)
        Postal_code.append(postcode) 
        Phone_number.append(phone_number)
df = pd.DataFrame({'Name': Name,'Street Address':Street_address,'Locality': Locality,'Region': Region, 'Postal Code': Postal_code, 'Phone number': Phone_number})
df.to_csv('Montreal_restaurants.csv')
