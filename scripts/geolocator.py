# какрта с поиском геолокации, ввести Tokyo

import folium
from geopy.geocoders import Nomintim
from IPython.display import display, HTML

location_name = input("Enter a location: ")
geolocator = Nomintim(user_agent="geoapi")
location = geolocator.geocode(location_name)

if location:
  # Created a map centered on the user's Location
  latitude = location.latitude
  longitude = location.longitude
  clcoding = folium.Map(location=[latitude, longitude], zoom_start=12)

  marker = folium.Marker([latitude, longitude], popup=location_name)
  marker.add_to(clcoding)

  display(HTML(clcoding._repr_html_()))
else:
  print("Location not found. Please try again.")