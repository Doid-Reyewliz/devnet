import urllib.parse
import requests

import folium

from gtts import gTTS
import os

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "fgGYLnYoy6g76rGg70oebyrNC9oGLytK"

# language = 'en'
# mytext = 'Welcome to geeksforgeeks!'
# myobj = gTTS(text=mytext, lang=language, slow=False)
# myobj.save("welcome.mp3")
# os.system("start welcome.mp3")



coordinates = [[-86.781247, 36.163532], [-80.191850, 25.771645]]
map_directions = folium.Map(location=[33.77, -84.37], zoom_start=5)

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break

    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("=============================================")
    
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
        
        folium.GeoJson(route, name='route').add_to(map_directions)
        folium.LayerControl().add_to(map_directions)
        print(map_directions)
        
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")