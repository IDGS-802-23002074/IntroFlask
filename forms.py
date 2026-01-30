from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField, RadioField
from wtforms import EmailField
from wtforms import validators
from flask_wtf import FlaskForm


class UserForm(Form):
    matricula= IntegerField('Matricula',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese un valor valido")
    ])
    nombre= StringField('Nombre',[
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=3, max=10, message="Ingrese un nombre válido")
    ])
    apaterno= StringField('Apaterno',[
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno= StringField('Amaterno',[
        validators.DataRequired(message="El campo es requerido")
    ])
    correo= EmailField('Correo',[
        validators.Email(message="Ingrese un correo valido")
    ])

class CinepolisForm(FlaskForm):
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El nombre es requerido"),
        validators.Length(min=3, max=30, message="Nombre inválido")
    ])

    compradores = IntegerField('Cantidad de compradores', [
        validators.DataRequired(message="Campo requerido"),
        validators.NumberRange(min=1, message="Debe haber al menos un comprador")
    ])

    boletos = IntegerField('Cantidad de boletos', [
        validators.DataRequired(message="Campo requerido"),
        validators.NumberRange(min=1, message="Debe comprar al menos un boleto")
    ])

    tarjeta = RadioField('Tarjeta Cinépolis',
        choices=[('si', 'Sí'), ('no', 'No')],
        default='no'
    )

