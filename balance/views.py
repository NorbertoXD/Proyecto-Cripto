from datetime import date, datetime, time
from flask import render_template, request, redirect, flash, url_for

from . import app
from .forms import Movimientosform
from .models import DBManager, CriptoModel

RUTA = 'data/balance.db'


@app.route("/")
def home():
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT * FROM movimientos")
    return render_template("inicio.html", movs=movimientos)



@app.route("/purchase", methods=["GET", "POST"])
def compra():
    
    if request.method == "GET":
        formulario = Movimientosform()
        return render_template("purchase.html", formulario=formulario)
    
    elif request.method == "POST":
        try:
            formulario = Movimientosform(data=request.form)
            moneda_from = formulario.moneda_from.data
            moneda_to = formulario.moneda_to.data
            cantidad_from = formulario.cantidad_from.data
            #cantidad_to = formulario.cantidad_to.data
            cripto_cambio = CriptoModel(moneda_from, moneda_to)
            consultar = cripto_cambio.consultar_cambio()
            total = cripto_cambio.cambio
            total = float(round(total, 10))
            
            cantidad_from = float(round(cantidad_from, 10))
            calculo = cripto_cambio.cambio
            calculo = float(round(calculo, 10))
            total = total*cantidad_from

            if formulario.consulta_api.data:

                    return render_template(
                        "purchase.html", formulario=formulario, 
                        numero=total, calculo=calculo
                        )
        except:
                return render_template(
                    "purchase.html", formulario=formulario, errores=[
                        "La consulta ha fallado"
                        ])

            
        if moneda_from == moneda_to:
            flash("Las monedas no pueden ser iguales", category='warning')
            return redirect(url_for("comprar"))

        db = DBManager(RUTA)
        cripto_cambio.moneda_from = moneda_from
        cripto_cambio.moneda_to = moneda_to
        cantidad_from = formulario.cantidad_from.data
        cambio = cripto_cambio.consultar_cambio()
        cantidad_to = cantidad_from * cambio

    
        
        if moneda_from == "EUR":
            saldo = float("inf")

        if saldo < cantidad_from:
            flash("Saldo insuficiente", category="warning")
            return redirect(url_for("comprar"))

        if formulario.consulta_api.data:
            formulario.cantidad_from.render_kw = {"readonly":True}
            return render_template(
                "form_movimiento.html", formulario = formulario,
                    cantidad_to = round(cantidad_to,5),
                    precio_unitario = round(cambio,5))

        elif formulario.cancelar.data:
            return redirect(url_for("comprar"))

        elif formulario.guardar.data:
            fecha = date.today().isoformat()
            hora = time(
                datetime.now().hour,
                datetime.now().minute,
                datetime.now().second)
            consulta = "INSERT INTO movimientos(fecha, hora, moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?, ?, ?, ?, ?, ?)"
            params = (
                fecha,
                str(hora),
                moneda_from,
                cantidad_from,
                moneda_to,
                cantidad_to)   
            resultado = db.consultaConParametros(consulta, params)
            
            if not resultado:
                return render_template(
                    'form_compra.html', formulario=formulario, id=id, errores=[
                        'Ha fallado la operación de guardar en la base de datos'])

            flash('Movimiento agregado correctamente ;)', category='exito')
            return redirect(url_for('movimientos'))






@app.route("/status", methods=["GET", "POST"])
def estado():
    return render_template("status.html")
