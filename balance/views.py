#from flask import render_template

from balance import app
#from .models import ListaMovimientos


@app.route('/')
def home():
    #movimientos = ListaMovimientos()
    #movimientos.leer_archivo()
    return "INICIOOOO"

@app.route('/purchase')
def compra():
    return "COMPRA"

@app.route('/status')
def estado():
    return "ESTADO"