from flask import Flask, render_template, send_from_directory
import Calculate

import threading

from os import environ
app = Flask(__name__)

@app.route('/')
def ServeIndex():
	return render_template("index.html")

@app.route('/graphs/<site>')
def FetchGraph(site):
	return send_from_directory('graphs', site + ".svg")

if __name__ == '__main__':

	app.run()
	# app.run(host='0.0.0.0') # Make server publicly visible