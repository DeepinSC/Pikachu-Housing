
import json
import urllib.request
import urllib.parse

def http_post(url,data):
	headers = {'content-type': 'application/json'}
	data = data.encode('utf-8')
	#print(data)
	req =  urllib.request.Request(url = url ,data = data,headers = headers)
	response = urllib.request.urlopen(req)
	print(response.getcodes())

data = """{"name": "601 E. Clark - 1 Bedroom - Available NOW!", "location": " 601 E Clark St, Champaign, IL, 61820, US", "price": 770, "imgs_url": ["5y14vbcv5yfieo4fyzitwl8h95atazsyybvu86430lquor1zvd.jpg", "2qu3z021l54qytv41a1aqdryds8ea13hmz5qacfqs7t5i0enh5.jpg", "p7dr0ln9jnx6mu3auzu6l5lj2at0g93crzps7cvmxd61hysywv.jpg", "imragc3q7fq2r6ee6e0hi3cyqvihpvwqecw8dqp4zso3a6q1oh.jpg", "uwo5r94uleg7d2aqzsklxtljxzt863c5lk78m6jm4vroi2c42d.jpg", "5c50i0lujl6tjilf3c6il7ozdeuht0ga5sok4z1foe8p7hmv85.jpg", "v1ruvbod0ydue3unzpep2tg9i1pruzcm8o5s2dn9tmx0cbwvow.jpg", "qk7bwoaa5ezbv57h8y8b8bzhz9x4o78rubt45yc7rasm4q7ys1.jpg", "5y14vbcv5yfieo4fyzitwl8h95atazsyybvu86430lquor1zvd.jpg", "2qu3z021l54qytv41a1aqdryds8ea13hmz5qacfqs7t5i0enh5.jpg", "p7dr0ln9jnx6mu3auzu6l5lj2at0g93crzps7cvmxd61hysywv.jpg", "imragc3q7fq2r6ee6e0hi3cyqvihpvwqecw8dqp4zso3a6q1oh.jpg", "uwo5r94uleg7d2aqzsklxtljxzt863c5lk78m6jm4vroi2c42d.jpg", "5c50i0lujl6tjilf3c6il7ozdeuht0ga5sok4z1foe8p7hmv85.jpg", "v1ruvbod0ydue3unzpep2tg9i1pruzcm8o5s2dn9tmx0cbwvow.jpg", "qk7bwoaa5ezbv57h8y8b8bzhz9x4o78rubt45yc7rasm4q7ys1.jpg", "ldgj3m9sjfbw01qo91qxvc6aw1spn1kgvnjvqhgye0zmgode7f.jpg", "nxyiny50aglddx8xw8zarkrm6uv6dz6caf29dqp12o83f9tknd.jpg", "j2jb3xni2vgp336kploxxg66uzm0htpofw7g18n5zyg94fr44i.jpg", "313nezt8cysk7175pewexvfxk8p9supp2tnxmhb2yue98pb1bm.jpg", "s78gfy3oqn90n6g6as5a01ex1c7qwa0cvvnj8e9rry4h3z1eww.jpg", "xzp7twjjm6hi9lh0wsulofjnu8p6n72tcej1uem6wxpw867nuj.jpg", "dageurznqxwobnv96b6pwoz0wte6aevlo2uw2v6iwlu3hrc4uq.jpg", "l3d2naxf5qljmn7827l72cmrsiwa9erlyiqo7qfuw73020lgmw.jpg", "gaqw88sxm6dgct93o9cf7o2rbnxmde6s6gr3m4wqpwxcolpwsk.jpg"], "types": "Size: 1 Bedrooms/1 Baths ", "description": "\n\nThese spacious one bedroom apartments features a large living/dining area that includes updated furniture and hard wood floors, a dining bar, and flat screen TV. They are located close to County Market and the University of Illinois Engineering Quad.\nRent includes monthly pest control, trash removal, access to the JSM Fitness Center and the JSM VIP Program with over $200 in savings, and a prompt, courteous, efficient maintenance staff. \n", "provider": 1, "latitude": 40.1151133, "longitude": -88.2301892086223, "cover_img": "https://apartments.jsmliving.com/uploads/application/images/500/"}"""
http_post("http://www.pikachu-housing.art/api/house/",data)