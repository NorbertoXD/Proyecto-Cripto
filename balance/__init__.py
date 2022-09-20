from flask import Flask
import requests


APIKEY = "b52eb9cea1044ad0a79b67e7e4f1e4c9"

#FICHERO = "balance/data/movimientos.csv"

app = Flask(__name__)
app.config.from_prefixed_env()