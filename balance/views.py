from . import app
from .models import ListaMovimientos



@app.route('/')
def home():
    lista_movimientos = ListaMovimientos()
    lista_movimientos.leer_archivo()
    return str(lista_movimientos)


@app.route('/purchase')
def compra():
    return "COMPRA"

@app.route('/status')
def estado():
    return "ESTADO"