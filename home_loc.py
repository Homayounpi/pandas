import pandas as pd
import numpy as np
import sqlite3
from haversine import haversine
import math
conection=sqlite3.connect('allStopNodes(1).db ')
df=pd.read_sql('SELECT * FROM  sample1',con=conection)
df['datetime']=pd.to_datetime(df['datetime'])
df['leaving_datetime']=pd.to_datetime(df['leaving_datetime'])
df=df[(df['datetime'].dt.hour>22)|(df['datetime'].dt.hour<7)]
df['lat']=df['lat'].apply(lambda x:math.ceil(x*10000)/10000)
df['lng']=df['lng'].apply(lambda x:math.ceil(x*10000)/10000)

df = df.groupby(['uid', 'lat', 'lng']).size().reset_index(name='count')
df['lat_1']=df['lat'].shift(-1)
df['lng_1']=df['lng'].shift(-1)
df['value']=np.where(df['uid']==df['uid'].shift(-1),'yes','no')
i=0

for index,row in df.iterrows():
    if row['value']=='yes':
        x=haversine((row['lat'],row['lng']),(row['lat_1'],row['lng_1']))
        df['value'].iloc[i]=x
    else:
        df['value'].iloc[i]=0
    i+=1

del df['lat_1']
del df['lng_1']
df=df.rename(columns={'value':'km'})
print(df.to_string())
# print(df.to_string())
# df.to_excel('uid_count_km.xlsx')


