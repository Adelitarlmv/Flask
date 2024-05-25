from flask import Flask
from flask import redirect
app =Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo desde Flask"

@app.route("/saludar")
def saludar():
    app.logger.info('Si efectivamente estamos aqui!!!')
    return "Hola Perdidas"

@app.route("/usuario/c")
def user(name):
    return "<h1>Hola:"+name+"</h1>"

@app.route("/direccion")
def redireccionar():
    return redirect("http://www.univalle.edu")

if __name__=='main':
    app.run(debug=True)