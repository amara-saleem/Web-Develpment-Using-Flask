from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hey this is practice for Flask Tutorial!"


app.run(debug=True)
