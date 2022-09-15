from flask import render_template

from . import app
from .models import ListaMovimientos



@app.route('/')
def home():
    movimientos = ListaMovimientos()
    movimientos.leer_archivo()
    return render_template("inicio.html", movs=movimientos.movimientos)


@app.route('/purchase')
def compra():
    return render_template("purchase.html")

@app.route('/status')
def estado():
    return render_template("status.html")
