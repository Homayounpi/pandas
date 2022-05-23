import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conect=sqlite3.connect('Normal StopNode from 2019-01-01 to 2020-12-30.db')
df=pd.read_sql("SELECT * FROM sample1",con=conect)
df['datetime']=pd.to_datetime(df['datetime'])
df['datetime']=df['datetime'].dt.floor('H')
df=df.sort_values(by='datetime')

df_main=df['datetime'].reset_index(name='time')
df_main=df_main[df_main['time'].dt.year==2019]
df_1=pd.read_excel('daily trajectori.xlsx')
df_main=df_main.groupby(pd.Grouper(key='time',freq='H')).size().reset_index(name='count')
df_main['hour']=df_main['time'].dt.hour
# df_main['year']=df_main['time'].dt.year
# df_main['month']=df_main['time'].dt.month_name()
df_main['day']=df_main['time'].dt.day
x=df_main.groupby('day')['count'].sum().reset_index(name='sumDaily')
df_main['sumDaily']=x['sumDaily']
x=df.groupby(['datetime','uid']).size().reset_index(name='useruniq')
x['useruniq']=1
x=x.groupby(['datetime','uid']).size().reset_index(name='cont')
df_main['useruniq']=x['cont']

x=df_main.apply(lambda w:df_main['sumDaily'].iloc[w['day']-1] ,axis=1).reset_index(name='useruniq')
df_main['sumDaily']=x['useruniq']
del df_main['day']
df_main['userOnImperssionPercent']=(df_main['count']/df_main['sumDaily'])/100000
df_main_19=df_main.groupby('hour')['count'].min().reset_index(name='count_19')

plt.plot(df_main_19['hour'],df_main_19['count_19'],marker='.')
plt.xlabel('hour')
plt.grid()
plt.show()








