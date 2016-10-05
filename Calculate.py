import requests
import xml.etree.ElementTree as ET
import json

def Calculate(site):
	bots_individual = ""
	bots_price = 0
	with open('bots.json') as json_file:
		bots_json = json.load(json_file)
		
	for bots_id in bots_json[site]:
		bots_individual = bots_individual + bots_id + ","

	q = requests.get("https://backpack.tf/api/IGetUsers/v3/?steamids=" + bots_individual)
	
	for bot in q.json()['response']['players']:
		try:
			value = q.json()['response']['players'][bot]['backpack_value']['440']
		except:
			value = 0
		
		bots_price = bots_price + value
	
	res_string = site + "'s estimated bot backpack value: " +  str(round(bots_price,2)) + " ref"
	
	return res_string
	
print(Calculate("market"))