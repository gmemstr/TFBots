from flask import Flask, render_template, send_from_directory, jsonify, request
import Calculate
from Analytics import Visitor

app = Flask(__name__)


@app.route('/')
def ServeIndex():
    Visitor(request.headers.get('User-Agent'), "PC", "PC")
    return render_template("index.html")


@app.route('/graphs/<site>')
def FetchGraph(site):
    return send_from_directory('graphs', site + ".svg")


@app.route('/raw/<res>')
def ReturnRawData(res):
    try:
        file = open("json/" + res + ".json", "r").read()
        return file
    except:
        return "not found"


if __name__ == '__main__':

    app.run()
    # app.run(host='0.0.0.0') # Make server publicly visible
