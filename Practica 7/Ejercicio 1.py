import requests

API_KEY = "4c9bd8239ccb6f916ec6e71758f57302"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def buscar():
    WIKIPEDIA = "https://es.wikipedia.org/api/rest_v1/page/summary/{ciudad}"
    
    ciudad = input("Escribe una ciudad: ").strip()
    
    if not ciudad:
        print("Aviso: Escribe una ciudad")
        return

    params = {
        "q": ciudad,
        "units": "metric",
        "appid": API_KEY,
        "lang": "es"
    }

    try:
        # Clima (OpenWeather)
        respuesta = requests.get(BASE_URL, params=params, timeout=10)
        data = respuesta.json()

        if data.get("cod") != 200:
            print("Error Clima: " + str(data.get("message")))
            return

        # Wikipedia
        ciudad_wiki = ciudad.title().replace(" ", "_")
        
        cabeceras = {'User-Agent': 'PracticaWebServices/1.0 (estudiante@ejemplo.com)'}
        
        respuesta_wikipedia = requests.get(WIKIPEDIA.format(ciudad=ciudad_wiki), headers=cabeceras, timeout=10)

        if respuesta_wikipedia.status_code == 200:
            datos_wiki = respuesta_wikipedia.json()

            print(f"\nCiudad: {data['name']}")
            print(f"Temperatura: {data['main']['temp']} °C")
            print(f"Clima: {data['weather'][0]['description']}\n")
            print(f"--- Wikipedia ---")
            print(f"Título: {datos_wiki['title']}")
            print(f"Descripción: {datos_wiki['extract']}")
            print(f"Enlace: {datos_wiki['content_urls']['desktop']['page']}")
        else:
            print(f"Clima OK, pero Wikipedia falló (Status: {respuesta_wikipedia.status_code})")

    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    buscar()