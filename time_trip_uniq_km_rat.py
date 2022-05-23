import pandas as pd
import sqlite3
df=pd.read_excel('Weekly trip rate.xlsx')
conecet=sqlite3.connect('Normal StopNode from 2019-01-01 to 2020-12-30.db')
db=pd.read_sql('SELECT * FROM sample1',con=conecet)
db['datetime']=pd.to_datetime(db['datetime'])
df=db.groupby(pd.Grouper(key='datetime',freq='W')).size().reset_index(name='trip')
df=df[df['trip']!=0]
x=db.groupby([pd.Grouper(key='datetime',freq='W'),'uid']).size().reset_index(name='uniq')
x=x.groupby('datetime')['uniq'].size().reset_index(name='uniq_1')
df=pd.merge(df,x,on='datetime')
x=db.groupby([pd.Grouper(key='datetime',freq='W')])['dr_km'].sum().reset_index(name='km')
x=x[x['km']!=0]
df=df.merge(x,on='datetime')
df['rate']=round((df['uniq_1']/df['trip']),2)
print(df.to_string())








