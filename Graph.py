import plotly.plotly as ply
import plotly.graph_objs as go
import json

with open("cache.json") as cache_file:
	cache_json = json.load(cache_file)

def GraphStocks():
	x = []
	y = []
	for time in cache_json:
		for site in cache_json[time]:
			x.append(time)	
			y.append(str(cache_json[time][site]) + " ref")
	
			data = [go.Scatter(x=x,y=y)]
			print(data)
			# ply.plot(data, filename = site + "stock")
		del x[:]
		del y[:]
GraphStocks()