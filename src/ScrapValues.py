import requests
import json
from Cache import Stash

backpacktf_key = ""


def RefinedValue():
    q = requests.get(
        "https://backpack.tf/api/IGetCurrencies/v1?key=" + backpacktf_key)
    prices = {}

    for item in q.json()['response']['currencies']:
        val = q.json()['response']['currencies'][item]['price']['value']
        prices[item] = val

    Stash(prices, "json/prices.json")
