import matplotlib.pyplot as plt
import json
import sys
import Cache


def InitGraphing():
    cache = Cache.Fetch("cache", "all")
    for site in cache[time]:
        GraphStocks(site)


def GraphStocks(site):

    cache = Cache.Fetch("cache", "all")
    keys = Cache.Fetch("prices")["keys"]
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
              str(prices[i - 1] / keys) + " keys")
    x = range(i)
    plt.xticks(x, history)
    plt.plot(x, prices, "g")

    plt.ylim(0)
    print("Saved as graphs/" + site + ".svg")
    plt.savefig("graphs/" + site + ".svg")
