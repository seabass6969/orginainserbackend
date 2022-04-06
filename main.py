import os
from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home_view():
        return "<h1>first</h1>"
@app.route("/test")
def test():
    return os.environ.get('TEST')
