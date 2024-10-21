from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Olá <br> Mundo!</h1>"

@app.route("/inicio")
def usuario ():
    return render_template('formulario.html')

@app.route("/envio", methods=['POST'])
def envioForms():
    nombre=request.form['username']
    password=request.form['password']
    if password == '123':
        return render_template('username.html', n=nombre)
    else:
        return render_template('formulario.html')
    