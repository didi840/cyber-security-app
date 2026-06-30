from flask import flask
app = flask(__name__)
@app.route(" / ")
def home():
    return "<h1>Welcome to my Website</h1>"

    app.run()