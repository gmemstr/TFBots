# TFBots (graphs branch)

### Working on README, any questions feel free to open an issue

Calculates estimates backpack values of TF2 trading bots.

### Requirements

Just run `pip install pip.txt` and pip will install the required 
Python libraries.

### Running

`python Calculate.py` will fetch all the data from backpack.tf
and cache it in cache.json.

`python Graph.py` will graph the data from the cache to a .png, 
requires you to change the value on line 26 to the site you
want to graph (temporary)

### Contributions

Know a good website that has trading bots? Add them to the bots.json
file as such:

```json
	"name": [
		"base64steamID1",
		"base64steamID2"
	]
```

Then create a new pull request for your fork.