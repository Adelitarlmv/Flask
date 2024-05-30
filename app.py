from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return render_template('pagina.html', title="Inicio Web UNIVALLE", mensaje="Hola de Nuevo")

@app.route('/')
def home():
    return render_template('index.html', title='Pagina APP UNIVALLE')

@app.route('/about')
def about():
    return render_template('about.html',title="Pagina acerca de Nosotros")

if __name__=='__main__':
    app.run(debug=True)