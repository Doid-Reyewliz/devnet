from geopy.geocoders import Nominatim
import openrouteservice as ors
import folium
import urllib.parse
import requests

from gtts import gTTS
import os


main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "fgGYLnYoy6g76rGg70oebyrNC9oGLytK"

loc = Nominatim(user_agent="GetLoc")

# orig = input("Starting Location: ")
# dest = input("Destination: ")

orig = "Aktobe Kazakhstan"
dest = "Almaty Kazakhstan"

origCoord = loc.geocode(orig)
destCoord = loc.geocode(dest)
    
coordinates = [[round(origCoord.longitude, 6), round(origCoord.latitude, 6)], [round(destCoord.longitude, 6), round(destCoord.latitude, 6)]]
# coordinates = [[76.945728, 43.236392], [74.607008, 42.876562]]

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

mytext = ''

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

client = ors.Client(key='5b3ce3597851110001cf6248ba2f26be1af44d1caa2482296fd38a6f')

route = client.directions(coordinates=coordinates, profile='driving-car', format='geojson')
map_directions = folium.Map()

folium.GeoJson(route, name='route').add_to(map_directions)
folium.LayerControl().add_to(map_directions)

# language = 'en'

# myobj = gTTS(text=mytext, lang=language, slow=False)

# myobj.save("welcome.mp3")

# os.system("welcome.mp3")

print(map_directions)



