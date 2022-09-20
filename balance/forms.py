from flask_wtf import FlaskForm
from datetime import date, datetime
from wtforms import HiddenField, SubmitField, DateField, TimeField, SelectField, FloatField
from wtforms.validators import DataRequired


class Movimientosform(FlaskForm):
    id = HiddenField()
    fecha = DateField()
    hora = TimeField()
   
    moneda_from = SelectField("Moneda_from: ", choices=[(
        "USD", "USD"), ("BTC", "BTC"), ("BNB", "BNB"), ("ETH", "ETH"), ("EUR", "EUR")],
        validators=[DataRequired(message="Tienes que seleccionar la moneda_from")])


    moneda_to = SelectField("Moneda_to: ", choices=[(
        "USD", "USD"), ("BTC", "BTC"), ("BNB", "BNB"), ("ETH", "ETH"), ("EUR", "EUR")],
        validators=[DataRequired(message="Tienes que seleccionar la moneda_to")])


    cantidad_from = FloatField(
        "cantidad_from: ", validators=
        [DataRequired(message="Cantidad de venta")])

    
    
    consultarapi = SubmitField("ConsultarAPI")
    
    enviar = SubmitField("Guardar")
    
    borrar = SubmitField("Borrar")