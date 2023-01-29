#This code can be used as a starting point for visualizing the location of a fire incident in real-time using the information from the fire drones.
#To integrate this code with the fire drone system, the following function can then be called and updated in real-time as the fire drones send 
#new location information. This way, a real-time map of the fire incidents can be generated, which can help emergency responders quickly assess 
#the extent of the fire and plan their response accordingly. This is just a basic example of how that might look like.

import folium

def coordinate_plotter(lat, long):
    map = folium.Map(location=[latitude, longitude], zoom_start=13)

    folium.Marker(location=[latitude, longitude]).add_to(map)

    display(map)
    
latitude = float(input("Enter latitude: "))
longitude = float(input("Enter longitude: "))
coordinate_plotter(latitude, longitude)
