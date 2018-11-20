import json
import urllib.request
import urllib.parse
from geopy.geocoders import Nominatim
import certifi
import ssl
import geopy.geocoders
import os
import http.client
def get_lat_and_long(loc):
	ctx = ssl.create_default_context(cafile=certifi.where())
	geopy.geocoders.options.default_ssl_context = ctx
	geolocator = Nominatim(user_agent="my_application")
	location = geolocator.geocode(loc)
	print(location)
	if location != None:
		return location.latitude,location.longitude
	return 0.0,0.0


get_lat_and_long("512 E Clark St., Champaign, IL US")