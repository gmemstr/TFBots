import matplotlib.pyplot as plt
import json
import sys

with open("json/cache.json") as cache_file:
	cache_json = json.load(cache_file)

def GraphStocks(site):
	plt.figure(1)
	plt.clf()
	history = []
	prices = []
	i = 0
	for time in sorted(cache_json):
		print("Result found at " + time)
		history.append(time)
		prices.append(cache_json[time][site])
		i = i + 1
	
	plt.ylabel('Value in refined metal')
	plt.title(site + " ref (total: " + str(prices[i - 1]) + ")")
	x = range(i)
	plt.xticks(x,history)
	plt.plot(x,prices,"g")
	
	print("Saved as graphs/" + site + ".png")
	plt.savefig("graphs/" + site + ".png")