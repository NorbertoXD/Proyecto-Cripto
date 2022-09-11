import csv

from . import FICHERO

class Movimiento:
    def __init__(self, fecha, hora, concepto, tipo, cantidad):
        self.fecha = fecha
        self.hora = hora
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

class ListaMovimientos:
    def __init__(self):
        self.lista_movimientos = []

    def leer_archivo(self):
        with open(FICHERO,"r", encoding="UTF-8") as fichero:
            reader = csv.DictReader(fichero)
            for linea in reader:
                self.lista_movimientos.append(linea)

