import matplotlib.pyplot as plt
import json
import sys
import time
import Cache


def InitGraphing():
    cache = Cache.Fetch("json/cache.json", "all")
    for site in cache[time.strftime("%x")]:
            GraphStocks(site)


def GraphStocks(site):
    cache = Cache.Fetch("json/cache.json", "all")
    keys = Cache.Fetch("json/prices.json")["keys"]
    metal = Cache.Fetch("json/prices.json")["metal"]
    plt.figure(1, figsize=(16, 6.67), dpi=75)
    plt.clf()
    history = []
    prices = []
    i = 0

    for time in sorted(cache)[-10:]:
        print("Result found at " + time)
        history.append(time)
        prices.append(cache[time][site])
        i = i + 1

    plt.ylabel('Value in refined metal')
    plt.title(site + " ref \nTotal: " + str(prices[i - 1]) + " refined " +
              str(round(prices[i - 1] / keys, 2)) + " keys $" +
              str(round(prices[i - 1] / metal, 2)) + " USD")
    x = range(i)
    plt.xticks(x, history)
    plt.plot(x, prices, "g")

    plt.ylim(0)
    print("Saved as graphs/" + site + ".svg")
    plt.savefig("graphs/" + site + ".svg")
