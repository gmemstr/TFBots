import time
import json

def Stash(data, filename):
	today = time.strftime("%x")
	# print(stocks)
	
	with open(filename) as cache:
		old = json.load(cache)
		
	old[today] = data
	
	with open(filename, "w") as cache:
		json.dump(old, cache, indent = 4)
	