# TFBots (graphs branch)

### Still revising README, feel free to open issues with questions

Calculates estimates backpack values of TF2 trading bots.

### Requirements

**Requires Python 3.x or higher. 2.x is not officially supported.**

Just run `pip install -r requirements.txt` and pip will install the required 
Python libraries. (`requests` and `matplotlib`)

### Running

`python Calculate.py` will fetch all the data from backpack.tf
and cache it in cache.json.

`python Graph.py (stn,scrap,market)` will graph the data of the
specific website to a .png in src/graphs/.

### Adding bots 

Know a good website that has trading bots? Add them to the bots.json
file as such:

```json
	"name": [
		"base64steamID1",
		"base64steamID2"
	],
```

Then create a new pull request for your fork.