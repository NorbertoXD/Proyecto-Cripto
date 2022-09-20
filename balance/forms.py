from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired


class Movimientosform(FlaskForm):
    id = HiddenField()
    fecha = HiddenField()
    hora = HiddenField()
    moneda_from = SelectField("Moneda_from: ", choices=[(
        "USD", "USD"), ("BTC", "BTC"), ("BNB", "BNB"), ("ETH", "ETH"), ("EUR", "EUR")],
        validators=[DataRequired(message="Tienes que seleccionar la moneda a vender")])

    cantidad_from = FloatField(
        "Moneda_from: ", validators=
        [DataRequired(message="Cantidad de venta")])

    
    moneda_to = SelectField("Moneda_to: ", choices=[(
        "USD", "USD"), ("BTC", "BTC"), ("BNB", "BNB"), ("ETH", "ETH"), ("EUR", "EUR")],
        validators=[DataRequired(message="Tienes que seleccionar la moneda to")])


    cantidad_to = FloatField(
        "Moneda_from: ", validators=
        [DataRequired(message="Cantidad de venta")])

    consulta_api = SubmitField("Consulta")


    cancelar = SubmitField(
        '✖', render_kw={'class':'green-button'})
    
    
    guardar = SubmitField("✔", render_kw={"class":"green-button"})