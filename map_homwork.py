import pandas as pd
import sqlite3
from haversine import haversine
import math
df=pd.read_excel('uid_count_km.xlsx')
conection=sqlite3.connect('allStopNodes(1).db ')
df_main=pd.read_sql('SELECT * FROM  sample1',con=conection)
df_main=df_main[['uid','lat','lng']]
df_main=df_main[df_main['uid'].isin(df['uid'])]
df_main['lat']=df_main['lat'].apply(lambda x:math.ceil(x*10000)/10000)
df_main['lng']=df_main['lng'].apply(lambda x:math.ceil(x*10000)/10000)
del df['km']
del df['Unnamed: 0']
df=df.sort_values(['uid','count'])
df=df[df['uid']!=df['uid'].shift(-1)]
# df.to_excel('uid_hom.xlsx')
df_main=df_main.groupby(['uid','lat','lng']).size().reset_index(name='count')
def uid(u):
    for i,row in df.iterrows():
        if row['uid']==u:
            return row['lat'],row['lng']
    else:
        return False
df_main['km_count']=df_main.apply(lambda x:(haversine((x['lat'],x['lng']),(uid(x['uid'])[0],uid(x['uid'])[1])))*x['count'],axis=1)
df_main=df_main.sort_values(['uid','km_count'])
df_main=df_main.sort_values(['count'])
df_main=df_main[df_main['uid']!=df_main['uid'].shift(-1)]
df_main=df_main.sort_values(['count'])
print(df_main.tail().to_string())






















