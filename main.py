from flask import Flask

app = Flask(__name__)

@app.route("/")
def index() :
    return "Hello"


@app.route("/testhit")
def index2() :
    return "Hello"