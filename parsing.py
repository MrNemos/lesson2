import csv
import requests

url = 'http://www.dsszzi.gov.ua/dsszzi/control/uk/index'
szua = requests.get(url)
with open('sz_ua.html','w',encoding='UTF-8') as file:
    file.write(szua.text)