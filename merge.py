#coding=utf8
import pandas as pd
file1=pd.read_csv('ly_no.csv',encoding='utf8')
file2=pd.read_csv('map_no.csv',encoding='utf8')
result=pd.merge(file1,file2,on='ID',how='inner')
result.to_csv('merge_lymap.csv',encoding='utf8')