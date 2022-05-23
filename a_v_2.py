import pandas as pd
import numpy as np
df=pd.read_excel('A9.xlsx')
df['value']=np.where(((abs(df['speed'].shift(-1)-df['speed'])<=1)&(df['datetime'].dt.date==df['datetime'].shift(1).dt.date))|
                     ((abs(df['speed'].shift(1)-df['speed'])<=1)&(df['datetime'].dt.date==df['datetime'].shift(1).dt.date)),'yes','no')
df['dr_km_old_1']=df['dr_km']
sum_km=0
sum_dt=0
sum_km_old=0
n=0
x=0
# print(df.to_string())
for i,j in df.groupby(['datetime','speed','value']):
    if j['value'].iloc[0]=='no':
        sum_km=0
        sum_dt=0
        n = n + 1
        x=0
        continue
    x+=1
    sum_km=sum_km+j['dr_km'].iloc[0]
    df.iloc[n,3]=sum_km
    df.iloc[n - x + 1, 12] = sum_km

    # df.iloc[n-x+1,17]=sum_km
    sum_dt = sum_dt + j['dt_min'].iloc[0]
    df.iloc[n,4]=sum_dt
    df.iloc[n - x + 1, 3] = sum_dt

    sum_km_old = sum_km_old + j['dr_km_old'].iloc[0]
    df.iloc[n, 5] = sum_km_old
    df.iloc[n - x + 1, 4] = sum_km_old

    df.iloc[n-x+1,6]=j['destination_lat'].iloc[0]
    df.iloc[n-x+1,7]=j['destination_lng'].iloc[0]
    df.iloc[n-x+1,9]=j['leaving_datetime'].iloc[0]
    df.iloc[n-x+1,2]=j['datetime'].iloc[0]
    n=n+1
df=df[(df['value']=='no')|((df['value']=='yes')&(df['value'].shift(1)=='no'))]
df['dr_km']=np.where(df['value']=='no',df['dr_km'],df['dr_km']-df['dr_km_old_1'])
df['speed_2']=(df['dr_km']/df['dt_min'])*60
df['acceleration']=np.where(df['datetime'].dt.date==df['datetime'].shift(-1).dt.date,(df['speed']-df['speed'].shift(-1))/df['dt_min'],0)
df['jerk ']=np.where(df['datetime'].dt.date==df['datetime'].shift(-1).dt.date,
                     (df['acceleration']-df['acceleration'].shift(-1))/df['dt_min'],0)
# df.to_excel('speed_acceleration.xlsx')
print(df.to_string())








