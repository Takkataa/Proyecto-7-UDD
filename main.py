import warnings # se importa para evitar advertencias no deseadas
from model import make_prediction # se importa del model.py la funcion que hace la predeccion de los datos
#Se importa flask junto con las librerias a utilizar
from flask import (
    Flask,
    request,
    jsonify
) 

warnings.filterwarnings('ignore')

app = Flask(__name__) 

#Se genera un metodo Get para confirmar que flash genero sin problemas la ruta
@app.route("/home_page", methods=["GET"]) 
def home_page():

    return "Hola Visiante"

#Se genera el metodo Post para ingresar los datos deseados al modelo
@app.route("/predict", methods=["POST"])
def predict():
    
    data = request.get_json()
    calificacion, acc = make_prediction(data)

    return jsonify({
        "La calificación de la aplicacion es": calificacion,
        "El porcentaje de Exactitud del modelo es de": acc,
    })

#Se inicializa la app
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )