import requests

print("=== OBTENIENDO EL CLIMA ===")

url_clima = "http://localhost:5000/clima?ciudad=Monterrey"
respuesta_clima = requests.get(url_clima)

if respuesta_clima.status_code == 200:
    datos = respuesta_clima.json()
    print(f"El clima en {datos.get('ciudad')}:")
    print(f" -> Temperatura: {datos.get('temperatura_celsius')} °C")
    print(f" -> Condición: {datos.get('condicion')}")
    print(f" -> Humedad: {datos.get('humedad_porcentaje')}%")
else:
    print("Error al contactar el servidor para el clima:", respuesta_clima.text)


print("\n=== ENVIANDO DATOS (POST) ===")
url_post = "http://localhost:5000/datos"
paquete_datos = {
    "practica 7": "Sistemas Distribuidos",
    "equipo": ["Lely", "Arantza"],
    "estatus": "Completado"
}

respuesta_post = requests.post(url_post, json=paquete_datos)
print("Lo que respondió el servidor:")
print(respuesta_post.json())
