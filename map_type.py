import pandas as pd
import datetime
import folium
df_main=pd.read_excel('A9.xlsx')
df=pd.read_excel('speed_acceleration.xlsx')
df=df[df['value']=='no']

x_=df_main['lat'].iloc[1]
y_=df_main['lng'].iloc[1]
m=folium.Map(location=[x_,y_],tiles='Stamen Terrain')
filter_id='+++1L7Sw9sHLT3jZwOtrJA=='
df=df[df['uid']==filter_id]

df['datetime']=pd.to_datetime(df['datetime'])
df['leaving_datetime']=pd.to_datetime(df['leaving_datetime'])
df_main['datetime']=pd.to_datetime(df_main['datetime'])
df_main['datetime']=pd.to_datetime(df_main['datetime'])
start_date=datetime.datetime(2020,7,2,0,1,1)
end_date=datetime.datetime(2020,7,3,23,59,59)
df=df[(df['datetime']>=start_date)&(df['leaving_datetime']<end_date)]
df_main=df_main[(df_main['datetime']>=start_date)&(df_main['leaving_datetime']<end_date)]
df=df_main.merge(df, how='outer', on='lat',indicator=True)
df['merg_-1']=df['_merge'].shift(-1)
df_2=df[(df['merg_-1'].isnull())|(df['_merge']=='both')|((df['_merge']=='left_only')&(df['_merge'].shift(-1)=='both'))]

def color_1(l):
    if 'both'==l:
        return 'green'
    return 'red'
for x,row in df.iterrows():
    folium.Marker(location=[row['lat'],row['lng_x']],popup=[row['datetime_x'],row['leaving_datetime_x']],
                 perfix='fa',
                  tooltip=[row['datetime_x'],row['leaving_datetime_x']],
                  icon=folium.Icon(color =color_1(row['_merge']))).add_to(m)
#=================================================================
def color_2(l,i):
    if (('both'==l)and(i=='both'))|(('both'==l)&('left_only'==i))|(('both'==i)&('left_only'==l)):
        return 'green'
    return 'red'
i=0
for lat,lng in zip(df['lat'],df['lng_x']):
    if i==len(df['lat'])-1:
        break
    folium.PolyLine([[df['lat'].iloc[i],df['lng_x'].iloc[i]],
                     [df['lat'].iloc[i+1],df['lng_x'].iloc[i+1]]],
                    color='red').add_to(m)
    i+=1

i=0
def lat(la,la_dis,merg):
    if merg!='both':
        return la_dis
    return la
def lng(ln,ln_dis,merg):
    if merg!='both':
        return ln_dis
    return ln
for _ in range(len(df_2)-1):
    folium.PolyLine([[df_2['lat'].iloc[i],df_2['lng_x'].iloc[i]],
                     [lat(df_2['lat'].iloc[i+1],df_2['destination_lat_x'].iloc[i+1],df_2['_merge'].iloc[i+1]),
                      lng(df_2['lng_x'].iloc[i+1],df_2['destination_lng_x'].iloc[i+1],df_2['_merge'].iloc[i+1])]]
                    ,color='green').add_to(m)
    i+=1
#=========================================================
df_2=df_2[df_2['_merge']!='both']
print(df_2.to_string())
for x,row in df_2.iterrows():
    folium.Marker(location=[row['destination_lat_x'],row['destination_lng_x']],popup=[row['datetime_x'],row['leaving_datetime_x']],
                 perfix='fa',
                  tooltip=[row['datetime_x'],row['leaving_datetime_x']],
                  icon=folium.Icon(color ='blue')).add_to(m)
for index,row in df_2.iterrows():
    folium.PolyLine([[row['lat'],row['lng_x']],
                   [row['destination_lat_x'],row['destination_lng_x']]],
                  color='red').add_to(m)
m.save('map3.html')








