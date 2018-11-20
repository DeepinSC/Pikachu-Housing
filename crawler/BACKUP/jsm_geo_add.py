import json
import urllib.request
import urllib.parse
from geopy.geocoders import Nominatim
import certifi
import ssl
import geopy.geocoders
import os
import http.client

def strip_redundency(loc,housing_type):
	new_loc = ''
	if housing_type == 1:
		if 'Location:' in loc:
			new_loc = loc.replace("Location:","")

	return new_loc

def get_lat_and_long(loc):
	ctx = ssl.create_default_context(cafile=certifi.where())
	geopy.geocoders.options.default_ssl_context = ctx
	geolocator = Nominatim(user_agent="my_application")
	#print(loc)
	location = geolocator.geocode(loc)
	print(location)
	if location != None:
		return location.latitude,location.longitude
	return 0.0,0.0
	#print(loca)
	#print(location.address)
	#print("Latitude:" + str(location.latitude))
	#print("Longitude:" + str(location.longitude))


#print(location.raw)
def http_post(url,data):
	headers = {'content-type': 'application/json'}
	
	data = data.encode('utf-8')
	#print(data)
	req =  urllib.request.Request(url = url ,data = data,headers = headers)
	response = urllib.request.urlopen(req)
	print(response.text)
	#print("Http code status: " + str(response.getcode()))
	#print(response.read().decode('utf-8'))


def rework_json(url,path,housing_type,domain):
	data = ''
	for itemName in os.listdir(path):
		if ".txt" in itemName:
			itemName = os.path.join(path,itemName)

			print(itemName)

			f = open(itemName,'r+')
			json_dict = json.loads(f.read())
			json_dict['provider'] = housing_type
			loc = strip_redundency(json_dict['location'],housing_type)
			json_dict['location'] = loc
			#print(loc)
			if loc != None or loc != '':
				latitude,longitude = get_lat_and_long(loc)
				json_dict['latitude'] = latitude
				json_dict['longitude'] = longitude

			if json_dict['imgs_url'] != None:
				#item_count = 0
				img_list = list()
				count = 0
				for i in range(0,len(json_dict['imgs_url'])):
					#item_count+=1
					if count > 24:
						break
					img_list.append(json_dict['imgs_url'][i].replace(domain,""))
					#count+=len(item)
					count+=1
					#print(len(item))
				#print("item_count" + str(item_count))
				#print(count)
				json_dict['imgs_url'] = img_list
			if len(json_dict['imgs_url']) > 0:
				json_dict['cover_img'] = domain
			data = json.dumps(json_dict)
			#print(data)
			http_post(url,data)
			#http_client_post(url,data)


URL = "http://www.pikachu-housing.art/api/house/"
PATH = "jsm_for_loop_json/"
DOMAIN = "https://apartments.jsmliving.com/uploads/application/images/500/"
HOUSING_TYPE = 1
rework_json(URL,PATH,HOUSING_TYPE,DOMAIN)
#f = urllib.request.urlopen(URL)
#print(f.read().decode('utf-8'))




		
		


