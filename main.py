
import datetime
from controladores.controlador_usuario import Lista, Listar, Incertar, buscando, Eliminar, Actualizar, edit
from flask import Flask, render_template, request, redirect, get_flashed_messages, flash
from controladores import controlador_usuario
app = Flask(__name__)

app.secret_key = "flash message"


@app.route("/")
def inicio():
    lista = Listar()

    return render_template("index.html", lista=lista)


@app.route("/insertar")
def insertar():

    return render_template("formulario_registrar.html")


@app.route("/Guardar", methods=['POST'])
def Guardar():
    fech = datetime.datetime.now()
    f = fech
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    cedula = request.form['cedula']
    fecha = f
    hora = f

    usuarios = Listar()
    usua = []

    

    if len(nombre) == 0 or len(apellido) == 0 or len(edad) == 0 or len(cedula) == 0:
        flash(' ⚠️Favor llene los espacios.....', 'info')
        return redirect("/insertar")
    try:
        for u in usuarios:
            print(u[3])
            usua.append(u[3])
        if cedula in usua:

            flash('⚠️ numero de cedula ya existente.....', 'info')
            return redirect("/insertar")

        else:
            Incertar(nombre, apellido, edad, cedula, fecha, hora)
            return redirect("/")
    except Exception as x:
        return redirect("insertar")


@app.route("/buscar", methods=['POST'])
def buscar():
    cedula = request.form['cedula']
    usuario = buscando(cedula)

    if(len(usuario) == 0):

        flash('⚠️ usuario no existe.....', 'info')
        return redirect("/")

    elif(usuario == usuario):

        return render_template("encontrado.html", usuario=usuario)


@app.route("/eliminar", methods=['POST'])
def eliminar():
    cedula = request.form['cedula']
    Eliminar(cedula)
    return redirect("/")


@app.route("/actualizar/<int:cedula>")
def actualizar(cedula):
    usuario = edit(cedula)

    print("usuario actualizar", usuario)
    return render_template("formulario_actualizar.html", usuario=usuario)


@app.route("/actualiza", methods=['POST'])
def actualiza():
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']

    Actualizar(nombre, apellido, edad,  codigo)

    return redirect("/")


if(__name__ == '__main__'):
    app.run(port='5000', debug=True)
