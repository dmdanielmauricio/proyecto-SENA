from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__=='__main__':
    app.run(debug=True)