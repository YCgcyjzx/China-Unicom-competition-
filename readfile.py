#coding=utf8
import pandas as pd
import time
reader=pd.read_table('/data/sjds7000.csv',encoding='utf-8',nrows=50000000,header=None)
reader1=reader.iloc[1:10000000]
date=[]
ID=[]
url=[]
day=[]
time=[]
URL=[]
for i in reader1[0]:
    a=i.split(',')
    date.append(a[0])
    ID.append(a[1])
    url.append(a[2])
for i in date:
    b=i.split()
    day.append(b[0])
    time.append(b[1])
for i in url:
    Web1=i.split('/',1)[0]
    URL.append(Web1.split('.', 1)[-1])
fil={'day':day,'time':time,'ID':ID,'URL':url}
DF=pd.DataFrame(fil)