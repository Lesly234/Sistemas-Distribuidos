from flask import Flask, jsonify, request
from flask_cors import CORS
import requests  

app = Flask(__name__)
CORS(app)

API_KEY = "cf0ab45dc3b937d9e73e2d1fffc6c12e" 

@app.route("/hola", methods=["GET"])
def hola_mundo():
    nombre_usuario = request.args.get("nombre", "Mundo")
    return jsonify({"mensaje": f"Hola, somos Arantza y Lesly"})

@app.route("/clima", methods=["GET"])
def clima():
    
    ciudad = request.args.get("ciudad", "Ciudad de Mexico")
    
    url_openweather = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"
    
    try:
        respuesta_ow = requests.get(url_openweather)
        datos_ow = respuesta_ow.json()
        
        if respuesta_ow.status_code == 200:
            clima_filtrado = {
                "ciudad": datos_ow["name"],
                "temperatura_celsius": datos_ow["main"]["temp"],
                "condicion": datos_ow["weather"][0]["description"],
                "humedad_porcentaje": datos_ow["main"]["humidity"]
            }
            return jsonify(clima_filtrado)
        else:
            # Si escriben mal la ciudad o la API key falla, mandamos el error de OpenWeather
            return jsonify({"error": "Fallo al consultar OpenWeather", "detalle": datos_ow}), respuesta_ow.status_code
            
    except Exception as e:
        return jsonify({"error": "Error interno del servidor", "detalle": str(e)}), 500

@app.route("/datos", methods=["POST"])
def recibir_datos():
    datos_recibidos = request.get_json()
    return jsonify({"Datos": datos_recibidos})

if __name__ == "__main__":
    app.run(port=5000)