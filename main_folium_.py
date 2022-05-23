import pandas as pd
import folium
import sqlite3
import datetime

conection=sqlite3.connect('allStopNodes.db')
df=pd.read_sql('SELECT * FROM sample1',con=conection)
df=df.head(70)

df['datetime']=pd.to_datetime(df['datetime'])
df['leaving_datetime']=pd.to_datetime(df['leaving_datetime'])

start=datetime.datetime(2020,1,1,23,1,1)
end=datetime.datetime(2021,1,1,23,1,1)

x_1=df['lat'].iloc[1]
y_1=df['lng'].iloc[1]

print(x_1,y_1)
ma_p=folium.Map(location=[x_1,y_1])

point_layer = folium.FeatureGroup(name="all")
point_layer_lin=folium.FeatureGroup(name='all_lin')

point_layer_1 = folium.FeatureGroup(name="green")
point_layer_1_lin=folium.FeatureGroup(name='green_lin')

point_layer_2 = folium.FeatureGroup(name="bron")
point_layer_2_lin=folium.FeatureGroup(name='bron_lin')

point_layer_3 = folium.FeatureGroup(name="marker")
point_layer_3_lin=folium.FeatureGroup(name='marker_lin')

df['lat_sh_1']=df['lat'].shift(-1)
df['lng_sh_1']=df['lng'].shift(-1)
df=df.dropna()
for i,row in df.iterrows():
    point_layer.add_child(folium.CircleMarker(location=[row['lat'],row['lng']],
    color='red',popup=f'lat:{row["lat"]} \n lng:{row["lng"]} \n {row["datetime"]}',tooltip=row['datetime'])).add_to(ma_p)
#[row['lat'],row['lng'],row['datetime']]
for i,row in df.iterrows():
    point_layer_lin.add_child(folium.PolyLine(locations=([row['lat'],row['lng']],
                                                     [row['lat_sh_1'],row['lng_sh_1']]),color='green')).add_to(ma_p)


filter_uid=['+8vtN3T+iKd4L1nUlBhsoB/u0rk=','0pNaf74J94OQ4goNFTcy6zi5a54=','34sv19qKipBk8OAuupcJnSu34oI=']
df=df[(df['datetime']>=start)&(df['datetime']<end)]
df=df[df['uid'].isin(filter_uid)]
for i,row in df.iterrows():
    point_layer_1.add_child(folium.CircleMarker(location=[row['lat'],row['lng']],
    color='green',popup=f'lat:{row["lat"]} \n lng:{row["lng"]} \n {row["datetime"]}',tooltip=row['datetime'])).add_to(ma_p)
for i,row in df.iterrows():
    point_layer_1_lin.add_child(folium.PolyLine(locations=([row['lat'],row['lng']],
                    [row['lat_sh_1'],row['lng_sh_1']]),color='#BFFF00')).add_to(ma_p)#green


for i,row in df.iterrows():
    point_layer_2.add_child(folium.CircleMarker(location=[row['lat'],row['lng']],
    color='brown',radius=30,fill_color='brown',popup=f'lat:{row["lat"]} \n lng:{row["lng"]} \n {row["datetime"]}',
                                                tooltip=row['datetime'])).add_to(ma_p)
for i,row in df.iterrows():
    point_layer_2_lin.add_child(folium.PolyLine(locations=([row['lat'],row['lng']],
                    [row['lat_sh_1'],row['lng_sh_1']]),color='#4D1A7F')).add_to(ma_p)#banafsh


for i,row in df.iterrows():
    point_layer_3.add_child(folium.Marker(location=[row['lat'],row['lng']],
                                          popup=f'lat:{row["lat"]} \n lng:{row["lng"]} \n {row["datetime"]}',
                                          tooltip=row['datetime'])).add_to(ma_p)
for i,row in df.iterrows():
    point_layer_3_lin.add_child(folium.PolyLine(locations=([row['lat'],row['lng']],
                            [row['lat_sh_1'],row['lng_sh_1']]),color='#FF3800')).add_to(ma_p)#narengi

ma_p.add_child(point_layer)
ma_p.add_child(point_layer_lin)

ma_p.add_child(point_layer_1)
ma_p.add_child(point_layer_1_lin)

ma_p.add_child(point_layer_2)
ma_p.add_child(point_layer_2_lin)

ma_p.add_child(point_layer_3)
ma_p.add_child(point_layer_3_lin)


ma_p.add_child(folium.LayerControl())

ma_p.save('uouys.html')


print('weq')