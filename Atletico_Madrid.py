import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import sys
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
con = MongoClient('localhost')
db = con.entity_db
coll = db.entities

url = "http://www.espnfc.com/club/atletico-madrid/1068/squad"
r = requests.get(url)
soup=BeautifulSoup(r.content)
table1 =soup.find_all('td',{'class':'pos'})
table =soup.find_all('td',{'class':'pla'})
for i,j in zip(table1,table):
    post=defaultdict(list)
    if j.a:
        x,y= i.text,j.a.text
    else:
        x,y=i.text,j.text
    attribute={'G':'goalkeeper','M':'midfielder','D':'defender','F':'attacker'}
    post['A'].append(y.strip().lower())
    post['EA_H']=[]
    post['T']=['person','footballer']
    post['mI']=defaultdict(list)
    #post['mI']['person']={'nationality':''}
    post['mI']['person']={'profession':'sportsman'}
    post['mI']['footballer']={'attribute':attribute[x]}
    post['mI']['footballer']['club']=['atletico madrid']
    print post
    try:
        #pass
        coll.insert(post)
    except DuplicateKeyError as e:
        print post
y='atletico madrid'
post=defaultdict(list)
post['A'].append(y.strip().lower())
post['EA_H']=[]
post['T']=['sportsteam']
post['mI']=defaultdict(list)
post['mI']['sportsteam']={'sport':'football'}
coll.insert(post)

