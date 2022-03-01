import phonenumbers
import folium
from number import number

#opencage api key : https://opencagedata.com/
key = "XX__YOUR_KEY__XX"

from phonenumbers import geocoder
cxNumber = phonenumbers.parse(number)
# Location
yourLocation = geocoder.description_for_number (cxNumber,'en')
print(f"Current Location(Country) : {yourLocation}.")

# ServiceProvider-Details
from phonenumbers import carrier
service_num_detail = phonenumbers.parse(number)
serviceProvider = carrier.name_for_number(service_num_detail,'en')
print(f"SERVICE PROVIDER : {serviceProvider}")

# MAP
from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(yourLocation)
results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(f"LATITUDE = {lat}")
print(f"LONGITUDE = {lng}")
print(f"[lat,long] = [{lat,lng}]")
# 
# MAP(folium):
yourMap =  folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourLocation).add_to(yourMap)
yourMap.save("locationMap.html")
# 
# ARUP MONDAL(@mondalCodeHub)