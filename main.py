from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms
import math

app = Flask(__name__)
app.secret_key='Clave secreta'
csrf=CSRFProtect()

@app.route('/')
def index():
    titulo="IDGS-802-flask"
    lista=['Juan','Karla','Miguel','Ana']
    return render_template('index.html',titulo=titulo,lista=lista)

@app.route('/usuarios', methods=["GET","POST"])
def usuarios():
    mat=0
    nom=''
    apa=''
    ama=''
    email=''
    usuarios_class=forms.UserForm(request.form)
    if request.method=='POST' and usuarios_class.validate():
        mat=usuarios_class.matricula.data
        nom=usuarios_class.nombre.data
        apa=usuarios_class.apaterno.data
        ama=usuarios_class.amaterno.data
        email=usuarios_class.correo.data

        mensaje='Bienvenido {}'.form(nom)
        flash(mensaje)

    return render_template('usuarios.html',form=usuarios_class,
                            mat=mat,nom=nom,apa=apa,ama=ama,email=email
                            )

@app.route('/formularios')
def formularios():
    return render_template('formulario.html')

@app.route('/reportes')
def reportes():
    return render_template('reportes.html')

@app.route('/hola')
def hola():
    return "Hola, Hola"

@app.route('/user/<string:user>')
def user(user):
    return "Hola, {user}"

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route('/user/<int:id>/<string:username>')
def username(id,username):
    return "ID: {} nombre: {}".format(id,username)

@app.route('/suma/<float:n1>/<float:n2>')
def func(n1,n2):
    return "La suma es: {}".format(n1+n2)

@app.route('/default/')
@app.route('/default/<string:param>')
def func2(param="juan"):
    return "Hola, {param}"

@app.route('/operas')
def operas():
    return """
     <form>
     <label for="name">Name:</label>
     <input type="text" id="name" name="name" required>

     <label for="name">apaterno:</label>
     <input type="text" id="name" name="name" required>
     </form>
     """


@app.route("/operasBas", methods=["GET","POST"])
def operas1():
    n1=0
    n2=0
    res=0
    if request.method == "POST":
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        res=float(n1)/float(n2)
    return render_template("operasBas.html",n1=n1,n2=n2,res=res)

@app.route("/resultado", methods=["POST"])
def resultado():
    n1 = float(request.form.get("n1"))
    n2 = float(request.form.get("n2"))
    operacion = request.form.get("operacion")

    if operacion == "suma":
        res = n1 + n2
        op = "Suma"
    elif operacion == "resta":
        res = n1 - n2
        op = "Resta"
    elif operacion == "multiplicacion":
        res = n1 * n2
        op = "Multiplicación"
    elif operacion == "division":
        if n2 == 0:
            return "No se puede dividir entre cero"
        res = n1 / n2
        op = "División"
    else:
        return "Operación no válida"

    return f"{op}: {res}"

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    distancia = None

    if request.method == "POST":
        x1 = float(request.form["x1"])
        y1 = float(request.form["y1"])
        x2 = float(request.form["x2"])
        y2 = float(request.form["y2"])

        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template("distancia.html", distancia=distancia)


@app.route("/cinepolis", methods=["GET", "POST"])
def cinepolis():
    total = None
    error = None
    max_boletos = None

    if request.method == "POST":
        compradores = int(request.form["compradores"])
        boletos = int(request.form["boletos"])
        tarjeta = request.form["tarjeta"]

        max_boletos = compradores * 7

        if boletos > max_boletos:
            error = f"No puede comprar más de {max_boletos} boletos."
        else:
            precio_boleto = 12
            subtotal = boletos * precio_boleto
            
            if boletos > 5:
                subtotal -= subtotal * 0.15
                
            elif boletos >= 3:
                subtotal -= subtotal * 0.10
                    
            if tarjeta == "si":
                subtotal -= subtotal * 0.10
                
            total = round(subtotal, 2)

    return render_template(
        "cinepolis.html",
        total=total,
        error=error,
        max_boletos=max_boletos
    )

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)