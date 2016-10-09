import requests
import xml.etree.ElementTree as ET
import json
import time

def Calculate():
	res_string = ""
	stocks = {}
	with open("json/bots.json") as json_file:
		bots_json = json.load(json_file)
	
	for site in bots_json:
		bots_individual = ""
		bots_price = 0
		for bots_id in bots_json[site]:
			bots_individual = bots_individual + bots_id + ","
	
		q = requests.get("https://backpack.tf/api/IGetUsers/v3/?steamids=" + bots_individual)
		print("\n" + site + " " +q.url)
		for bot in q.json()['response']['players']:
			try:
				value = q.json()['response']['players'][bot]['backpack_value']['440']
			except:
				value = 0
			
			bots_price = bots_price + value
		
		res_string = res_string + "\n" + site + "'s value: " + str(round(bots_price, 2))
		
		stocks[site] = round(bots_price, 2)
		
	Cache(stocks)
	return res_string
	
def Cache(stocks):
	today = time.strftime("%x")
	print(stocks)
	
	with open('json/cache.json') as cache:
		old = json.load(cache)
		
	old[today] = stocks
	
	with open("json/cache.json", "w") as cache:
		json.dump(old, cache, indent = 4)
	
print(Calculate())