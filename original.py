import requests
import xml.etree.ElementTree as ET
import json

bots_total = 41
bots_price = 0
bots_individual = ""
i = 1

while i < bots_total:
	r = requests.get("https://steamcommunity.com/id/shopbot" + str(i) + "?xml=1")
	root = ET.fromstring(r.text)
	
	if root[0].text == "The specified profile could not be found.":
		print("tf2scrap" + str(i) + " could not be found.")
	else:
		# print("tf2scrap" + str(i) + " found.")
		bots_individual = bots_individual + root[0].text + ","
		print('"' + root[0].text + '",')

	i = i + 1

q = requests.get("https://backpack.tf/api/IGetUsers/v3/?steamids=" + bots_individual)

# For debugging
# print(q.json()['response']['players']['76561198068475408']['backpack_value'])

for bot in q.json()['response']['players']:
	try:
		value = q.json()['response']['players'][bot]['backpack_value']['440']
	except:
		value = 0
		
	bots_price = bots_price + value
	
print(bots_price)