# TFBots

[Live Website](http://tfbots.trade)

Calculates & graphs estimated backpack values of TF2 trading bots over time.

### Requirements

**Requires Python 3.x or higher. 2.x is not officially supported.**

Just run `pip install -r requirements.txt` and pip will install the required 
Python libraries. (`requests`, `matplotlib` and `flask`)

### Running

`python Calculate.py` will fetch all the data from backpack.tf
and cache it in cache.json, then run the caching scripts. It will
then start a thread that auto reruns the script every 24 hours.


`python Webserver.py` will start up the webserver that will display
the graphs is an organised fashion at `localhost:8080`. 

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