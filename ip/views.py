from django.shortcuts import render
import requests
import folium

# Create your views here.
def home(request):
    if request.method == 'POST':
        ip_addr = requests.get("https://api.ipify.org").text
        api_key = "5be5f0b470c4d878afed50b1c21a0940"
        location_details = requests.get(f"http://api.ipstack.com/{ip_addr}?access_key={api_key}").json()
        latitude = location_details["latitude"]
        longitude = location_details["longitude"]
        location = f"{location_details['city']}, {location_details['region_name']}, {location_details['country_name']}, PINCODE - {location_details['zip']}"
        worldmap = folium.Map()
        folium.Marker([latitude,longitude]).add_to(worldmap)
        htmlcode = worldmap._repr_html_()
        context = {'map':htmlcode, 'location':location, 'ip':ip_addr}
        return render(request,'ip/home.html',context)
    if request.method == 'GET':
        return render(request,'ip/home.html')