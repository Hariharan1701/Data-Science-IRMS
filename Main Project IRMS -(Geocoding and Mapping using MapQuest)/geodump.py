import sqlite3
import json

conn = sqlite3.connect('geocode_data')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
results = cur.fetchall()

fhand = open('where.js', 'w')
fhand.write("mydata = [\n")
count = 0
for row in results:
    where = row[0]
    where = where.replace("'", " ").strip()
    lat = row[1]
    lng = row[2]
    if lat == 0 or lng == 0: continue
    try:
        count = count + 1
        output = "[" + str(lat) + "," + str(lng) + ", '" + where + "'],\n"
        print(output)
        fhand.write(output)
    except:
        continue
    else:
        pass
fhand.write("];\n")
cur.close()
fhand.close()

print(count, "records written to where.js")
print("Open where.html to view the data in a browser")