from flask import Flask

app = Flask(__name__)

@app.route("/about")
def about():
    return "<p>This is Rally</p>"

