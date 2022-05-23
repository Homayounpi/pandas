import folium

m=folium.Map(location=[45.5236, -122.6750], zoom_start=13)

map=folium.Map(location=[37.296933,-121.9574983],zoom_start=8)
folium.Marker(location=[37.4074687,-122.086669],
              popup = "Google HQ", icon=folium.Icon(color = 'gray')).add_to(map)

for i in [[37.4074687,-122.086669],[37.8199286,-122.4804438]]:
    folium.CircleMarker(location=i,radius = 9,fill_color='green',color="red").add_to(map)#"Mapbox bright"

map1 = folium.Map(location=[55.406980,-3.56234], zoom_start=13,tiles='Stamen Terrain')#'#cartodbpositron
folium.CircleMarker(location=[55.621470,-3.85645]).add_to(map1)
folium.CircleMarker(location=[55.788410,-4.03430]).add_to(map1)
folium.PolyLine([[55.621470,-3.85645],[55.788410,-4.03430]]).add_to(map1)
map1.save("index.html")








