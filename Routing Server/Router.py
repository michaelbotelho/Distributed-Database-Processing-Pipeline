import requests

from flask import Flask


app = Flask(__name__)


@app.route('/')
def Route():
    print("Temp")