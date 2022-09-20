import sqlite3
import requests
from criptocambio import APIKEY 



class DBManager:
    def __init__(self, ruta):
        self.ruta = ruta

    
    def consultaSQL(self, consulta):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        cursor.execute(consulta)
        self.movimientos = []
        nombres_columnas = []

        for desc_columna in cursor.description:
            nombres_columnas.append(desc_columna[0])

        
        datos = cursor.fetchall()
        for dato in datos:
            movimiento = {}
            indice = 0
            for nombre in nombres_columnas:
                movimiento[nombre] = dato[indice]
                indice += 1
            self.movimientos.append(movimiento)

        conexion.close()

        return self.movimientos



    def consultaConParametros(self, consulta, params):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = False
        try:
            cursor.execute(consulta, params)
            conexion.commit()
            resultado = True
        except Exception as error:
            print("ERROR DB:", error)
            conexion.rollback()
        conexion.close()

        return resultado

    

    def solicitudConParametros(self, consulta, params):
        conexion = sqlite3.connect(self.ruta)
        cursor = conexion.cursor()
        resultado = 0
        try:
            cursor.execute(consulta, params)
            dato = cursor.fetchone()
            dato = dato[0]
            if dato == None:
                dato = 0
            resultado = dato
        except Exception as error:
            print("ERROR DB:", error)

        conexion.close()

        return resultado


class APIError(Exception):
    pass



class CriptoModel: 

    def __init__(self):
        self.moneda_from = ""
        self.moneda_to = ""
        self.cambio = 0.0


    def consultar_cambio(self):
        headers = {
            'X-CoinAPI-Key': APIKEY
            }

        url = f"http://rest.coinapi.io/v1/exchangerate/{self.moneda_from}/{self.moneda_to}"
        respuesta = requests.get(url, headers=headers)

        if respuesta.status_code == 200:
            self.cambio = respuesta.json()["rate"]
        else:
            raise APIError(
                "Ha ocurrido un error {} {} al consultar la API.".format(
                    respuesta.status_code, respuesta.reason))
        