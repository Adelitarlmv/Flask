from flask import Flask
from flask import redirect
from flask import jsonify, abort
app =Flask(__name__)

# Datos de ejemplo
users = {
    1: {"name": "Peter Parker", "email": "john@example.com"},
    2: {"name": "Mary Jane Watson", "email": "jane@example.com"}
}


@app.route("/")
def index():
    return "Hola Mundo desde Flask"

@app.route("/saludar")
def saludar():
    app.logger.info('Si efectivamente estamos aqui!!!')
    return "Hola Perdidas"

@app.route("/usuario/<name>")
def user(name):
    return "<h1>Hola:"+name+"</h1>"

@app.route("/direccion")
def redireccionar():
    return redirect("http://www.univalle.edu")

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user=users.get(user_id)
    if user is None:
        abort(404, description="Usuario no Encontrado")
    return jsonify(user)
   
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error":str(error)}),404 

if __name__=='main':
    app.run(debug=True)