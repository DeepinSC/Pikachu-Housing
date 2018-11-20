
import requests
import urllib.request
from bs4 import BeautifulSoup
import json

def write_to_json(name,location,price,imgs_url,types,description,provider):
	json_dict = dict()
	json_dict["name"] = name
	json_dict["location"] = location
	json_dict["price"] = price
	json_dict["imgs_url"] = imgs_url
	json_dict["types"] = types
	json_dict["description"] = description
	json_dict["provider"] = provider
	return json.dumps(json_dict)

def append_to_file(path, data):
	with open(path,'a') as file:
		file.write(data + '\n')

def write_file(file_name,data):
	f = open(file_name,'w')
	f.write(data)
	f.close()
	#print("HIT")
	f.close()
def imgLink_to_file(file_name,img_list):
	f = open(file_name,'a')
	for link in sorted(img_list):
		append_to_file(file_name,link)
	f.close()

def remove_header_tag(header,h_tag_one, h_tag_two):
	header = str(header)
	header = header.replace(h_tag_one,"")
	header = header.replace(h_tag_two,"")
	return header

def findImage(url, domain, i):
	apt_info_list = list()
	img_list = list()
	apt_info =''
	apt_address = ''
	apt_price = ''
	apt_detail = ''
	apt_stat = list()
	counter = 0
	r = requests.get(url)
	html_content = r.text
	soup = BeautifulSoup(html_content,"html.parser")
	info = soup.find_all("div",{"class": "info"})
	stats = soup.find_all("div",{"class":"stats"})
	desc = soup.find_all("div",{"class": "description"})

	for de in desc:
		apt_detail = de.text.replace("\u00a0"," ")
	for stat in stats:
		for s in stat.find_all("div",{"class":"stat"}):
			apt_stat.append(remove_header_tag(s,"""<div class="stat">""","</div>"))

			#print(s)
			#<div class="stat">Size: 3 Bedrooms/2 Baths </div>
			#<div class="stat">$1,730</div>
			#<div class="stat">Fall 2019/20</div>
	for loc in info:
		for addr1 in loc.find_all('h1'):
			apt_info = remove_header_tag(addr1,"<h1>","</h1>")
		for addr2 in loc.find_all('h2'):
			apt_address = remove_header_tag(addr2,"<h2>","</h2>")
	for img in soup.find_all('img'):
		img_url = img.get('src')
		if "/uploads/application" in img_url:
			img_url = domain + img_url
			img_list.append(img_url)
	file_name = "jsm_for_loop_json/"+str(i)+'.txt'
	apt_description = apt_info + "@"+ apt_address
	if "Parking" in apt_description:
		return;
	if apt_address == "" or apt_info == "" or apt_stat == "" :
		return;
	print(apt_info)
	#"Please select your suite" does not have pictures
	apt_price = apt_stat[1].replace("$","")
	if "," in apt_price:
		apt_price = apt_price.replace(",","")
	apt_price = apt_price[:4]
	if " " in apt_price:
		apt_price = apt_price.replace(" ","")
	if apt_price.isdigit() == True:
		apt_price = int(apt_price)
	else:
		apt_price = int("-1")
	#print(write_to_json(apt_info,apt_address,apt_price,img_list,apt_stat[0],apt_detail,"jsmliving"))
	write_file(file_name,write_to_json(apt_info,apt_address,apt_price,img_list,apt_stat[0],apt_detail,"jsmliving"))


#url = "https://apartments.jsmliving.com/apartments/?unit_type_id=13"
#findImage(url,"https://apartments.jsmliving.com","0")
for i in range(0,1000):

	url = "https://apartments.jsmliving.com/apartments/?area=0&unit_type_id=%s" %i
	print(str(i) + ":")
	findImage(url,"https://apartments.jsmliving.com",i)
	
