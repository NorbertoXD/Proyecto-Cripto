from flask import render_template, request

from . import app
from .models import DBManager

RUTA = 'data/balance.db'


@app.route("/")
def home():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT * FROM movimientos")
    return render_template("inicio.html", movs=movimientos)



@app.route("/purchase", methods=["GET", "POST"])
def compra():
    if request.method == "GET":
        return render_template("purchase.html")
    #else:
        #¿return " he llegado aqui gracias a post"



@app.route("/status", methods=["GET", "POST"])
def estado():
    return render_template("status.html")
