from flask import render_template

from . import app
from .models import ListaMovimientos


@app.route('/')
def inicio():
    movimientos = ListaMovimientos()
    movimientos.leer_archivo()
    