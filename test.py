import openrouteservice

coords = ((8.34234,48.23424),(8.34423,48.26424), (8.34523,48.24424), (8.41423,48.21424))

client = openrouteservice.Client(key='5b3ce3597851110001cf6248ba2f26be1af44d1caa2482296fd38a6f') # Specify your personal API key
routes = client.directions(coords, profile='cycling-regular', optimize_waypoints=True)

print(routes)