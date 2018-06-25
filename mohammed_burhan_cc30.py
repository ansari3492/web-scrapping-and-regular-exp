# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:26:06 2018

@author: Lenovo
"""

import urllib.request

icc="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
page=urllib.request.urlopen(icc)
from bs4 import BeautifulSoup
soup=BeautifulSoup(page)
all_tables=soup.find_all('table')
right_table=soup.find('table',class_='table')
#generate list
a=[]
b=[]
c=[]
d=[]
e=[]

for row in right_table.find_all('tr'):
    cells=row.find_all('td')
    if len(cells)==5:
        a.append((cells[0]).text.strip())
        b.append((cells[1]).text.strip())
        c.append((cells[2]).text.strip())
        d.append((cells[3]).text.strip())
        e.append((cells[4]).text.strip()) 

    

import pandas as pd
df=pd.DataFrame(a,columns=['Number'])
df['pos']=a
df['team']=b
df['matches']=c
df['points']=d
df['rankings']=e
print(df)

