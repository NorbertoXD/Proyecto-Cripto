from flask import Flask


app = Flask(__name__)


@app.route('/')
def hola():
    return "Hola, soy Flask ¿ y tu ?"