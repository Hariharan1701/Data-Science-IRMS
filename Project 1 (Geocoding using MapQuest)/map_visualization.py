from folium.map import Icon, Popup
import pandas as pd
import folium
from folium.plugins import MarkerCluster

m = folium.Map(location=[12.86725,80.22186], tiles='OpenStreetMap', zoom_start = 5)

# 
# folium.Marker(location=[48.86762,2.3624], Popup='TEXT' , icon = folium.Icon(color='blue')).add_to(m)
# folium.Marker(location=[49.86762,2.3624], Popup='TEXT' , icon = folium.Icon(color='red')).add_to(m)
 
MarkerCluster = MarkerCluster().add_to(m)
df = pd.read_csv('geodata.csv')
#print(df.head())

for i,row in df.iterrows():
    lat = df.at[i,'lat']
    lng = df.at[i,'lng']
    clg_name = df.at[i,'Name']
    
    popup = df.at[i, 'Name'] + '<br>' + str(df.at[i,'State']) + '<br>' + str(df.at[i,'Country'])
    
    folium.Marker(location=[lat,lng], popup=popup , icon = folium.Icon(color='red')).add_to(MarkerCluster)
    
m.save('index.html')    