import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urlparse
import csv
import ftplib
import os
import time


#url = 'http://g1.globo.com/dynamo/rio-de-janeiro/rss2.xml'
#r = requests.get(url)
#soup = BeautifulSoup(r.content, 'xml')
#artigo = soup.find_all('item')

#for i in artigo:
#     titulo = i.title.text
#     data = i.pubDate.text
#     link = i.link.text
#     texto = i.description.text
#     imagem = i.find('content')

     #print(imagem)

url = 'https://noticias.r7.com/rio-de-janeiro/feed.xml'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'xml')
artigo = soup.find_all('entry')
for i in artigo:
     titulo = i.title.text
     data = i.updated.text
     link = i.link.text
     texto = i.content.text
     imagem = i.find('img', class_='croppable')
     print(texto)
     exit()


#    print(titles[i].get_text(),"by",end=' ')
#    print(authors[i].get_text(),end=' ')
#    print("costs $" + prices[i].get_text())
