import requests

API_KEY_WEATHER = "4c9bd8239ccb6f916ec6e71758f57302"
BASE_URL_WEATHER = "https://api.openweathermap.org/data/2.5/weather"
GEONAMES_USER = "lesly29" 
GEONAMES_URL = "http://api.geonames.org/searchJSON"

def buscar():
    WIKIPEDIA = "https://es.wikipedia.org/api/rest_v1/page/summary/{ciudad}"
    
    ciudad = input("Escribe una ciudad: ").strip()
    
    if not ciudad:
        print("Aviso: Escribe una ciudad")
        return

  
    params_geo = {
        "q": ciudad,
        "maxRows": 1,
        "username": GEONAMES_USER,
        "lang": "es",
        "featureClass": "P" 
    }

    # Parámetros para OpenWeather
    params_weather = {
        "q": ciudad,
        "units": "metric",
        "appid": API_KEY_WEATHER,
        "lang": "es"
    }

    try:
        resp_geo = requests.get(GEONAMES_URL, params=params_geo, timeout=10)
        data_geo = resp_geo.json()
        
        pais = "No encontrado"
        poblacion = "No disponible"
        
        if data_geo.get("geonames"):
            info_geo = data_geo["geonames"][0]
            pais = info_geo.get("countryName", "No encontrado")
            poblacion = info_geo.get("population", "No disponible")

        respuesta = requests.get(BASE_URL_WEATHER, params=params_weather, timeout=10)
        data = respuesta.json()

        if data.get("cod") != 200:
            print("Error Clima: " + str(data.get("message")))
            return

        ciudad_wiki = ciudad.title().replace(" ", "_")
        cabeceras = {'User-Agent': 'PracticaWebServices/1.0 (estudiante@ejemplo.com)'}
        respuesta_wikipedia = requests.get(WIKIPEDIA.format(ciudad=ciudad_wiki), headers=cabeceras, timeout=10)

        print(f"\nCiudad: {data['name']}")
        print(f"País: {pais}")
        print(f"Población: {poblacion}")
        print(f"Temperatura: {data['main']['temp']} °C")
        print(f"Clima: {data['weather'][0]['description']}\n")

        if respuesta_wikipedia.status_code == 200:
            datos_wiki = respuesta_wikipedia.json()
            print(f"--- Wikipedia ---")
            print(f"Título: {datos_wiki['title']}")
            print(f"Descripción: {datos_wiki['extract']}")
            print(f"Enlace: {datos_wiki['content_urls']['desktop']['page']}")
        else:
            print(f"Clima OK, pero Wikipedia falló.")

    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    buscar()