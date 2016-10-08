import matplotlib.pyplot as plt
import json

with open("json/cache.json") as cache_file:
	cache_json = json.load(cache_file)

def GraphStocks(site):
	plt.figure(1)
	history = []
	prices = []
	i = 0
	for time in sorted(cache_json):
		print(time)
		history.append(time)
		prices.append(cache_json[time][site])
		i = i + 1
	
	plt.ylabel('Value in refined metal')
	plt.title(site + " ref"	)
	x = range(i)
	plt.xticks(x,history)
	plt.plot(x,prices,"g")
	
	plt.savefig("graphs/" + site + ".png")

GraphStocks("market")