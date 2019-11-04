import folium
import pandas
data = pandas.read_csv("colleges.txt")
lat = list(data["Latitude"])
lon  = list(data["Longitude"])
name = list(data["Name"])
p = list(data["Place"])
st = list(data["State"])
cou = list(data["Country"])
rn = list(data["Rank"])

def color(r):
    if 1<= r <5:
        return 'green'
    elif 5<= r <10:
        return 'orange'
    elif 10<=r<15:
        return 'red'
    else:
        return 'blue'

html = """<div style = "font-size:large;font-color:yellow;font-weight:bolder,font-family:Monospace">Name: {}<br/>Rank: {}<br/>Location: {}, {}, {}</div>"""

map = folium.Map(location=[27.7,85.3], zoom_start=80,tiles="OpenStreetMap")

fg = folium.FeatureGroup(name = "My Map")

for lt,ln,name,rn,p,st,cou in zip(lat,lon,name,rn,p,st,cou):
    iframe  = folium.IFrame(html = html.format(str(name),str(rn),str(p),str(st),str(cou)),width=300,height = 200)
    fg.add_child(folium.Marker(location=[lt,ln],popup = folium.Popup(iframe),icon = folium.Icon(color = color(rn))))

map.add_child(fg)


map.save("Map1.html")
