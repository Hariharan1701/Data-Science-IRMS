import urllib.request
import urllib.parse
import sqlite3
import json
import time
import requests

API_KEY = 'QIjeaW1BRRsZMsZ8LFrEu7TMtmZlQGrC'
base_url = 'http://www.mapquestapi.com/geocoding/v1/address?'

db=sqlite3.connect('geocode_data')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Locations (College_Name TEXT, lat number, lng number)''')

fhand=open('where.data')

for line in fhand:
    js=''
    address = line.strip()
    params=urllib.parse.urlencode({'location' : line, 'key' : API_KEY })
    url = f'{base_url}{params}'
    print("Retrieving : ",url)

    response = requests.get(url)

    data = response.content.decode('utf-8')#.replace("'", '"')

    js = json.loads(data)
    #print(js)
    lat = js['results'][0]['locations'][0]['latLng']['lat']
    lng = js['results'][0]['locations'][0]['latLng']['lng']
    #print (lat,lng)
    #print(lat, lng)
    #print(data)

    cur.execute("""INSERT INTO Locations (College_Name,lat,lng) VALUES ('{}',{},{})""".format(line,lat,lng))

    db.commit()
    time.sleep(1)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
