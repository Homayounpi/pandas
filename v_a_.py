import pandas as pd
import numpy as np

df=pd.read_excel('test1.xlsx')
df=df.dropna(how='all')
df=df.rename(columns={'Unnamed: 1':'rowid','Unnamed: 2':'lat','Unnamed: 3':'lng','Unnamed: 6':'dr_km_old',
                      'Unnamed: 12':'origin','Unnamed: 13':'destination','Unnamed: 15':'year','Unnamed: 16':'month',
                      'Unnamed: 17':'type','Unnamed: 18':'NaN','Unnamed: 14':'dr_km','Unnamed: 5':'dt_min',
                      'Unnamed: 19':'speed','Unnamed: 11':'leaving_datetime','Unnamed: 10':'uid','Unnamed: 4':'datetime',
                      'Unnamed: 8':'destination_lat','Unnamed: 9':'destination_lng'})

df_main=df[['uid','leaving_datetime','dr_km','dt_min','datetime','lng','lat']]
df_main=df_main.sort_values(by=['uid','leaving_datetime'])

df_main=df_main.head(-1)
df_main['leaving_datetime']=pd.to_datetime(df_main['leaving_datetime'])
df_main['speed']=(df_main['dr_km']/df_main['dt_min'])*60
df_main['acceleration']=((df_main['speed'].shift(-1)-df_main['speed'])/df_main['dt_min']).fillna(0)
df_main['jerk']=(df_main['acceleration'].shift(-1)-df_main['acceleration'])/df_main['dt_min']
df_main['speed'].iloc[1:10]=1
df_main['acceleration'].iloc[1:10]=1
df_main['jerk'].iloc[1:10]=1
df_main['value']=np.where((abs(df_main['speed'].diff(-1))<=1)&
                          (abs(df_main['acceleration'].diff(-1))<= 1)&
                          (abs(df_main['jerk'].diff(-1)) <= 1)&
                         (df_main['uid']==df_main['uid'].shift(-1)),'yes','no')
df_main['leaving_datetime']=np.where(df_main['value']=='yes',df_main['leaving_datetime'].shift(-1),df_main['leaving_datetime'])
df_main['lat']=np.where(df_main['value']=='yes',df_main['lat'].shift(-1),df_main['lat'])
df_main['lng']=np.where(df_main['value']=='yes',df_main['lng'].shift(-1),df_main['lng'])
df_main=df_main[df_main['leaving_datetime']!=df_main['leaving_datetime'].shift(1)]

df_main['speed']=df_main['speed'].apply(lambda x:round(x,2))
df_main['acceleration']=df_main['acceleration'].apply(lambda x:round(x,2))
df_main['jerk']=df_main['jerk'].apply(lambda x:round(x,2))
print(df_main.to_string())

