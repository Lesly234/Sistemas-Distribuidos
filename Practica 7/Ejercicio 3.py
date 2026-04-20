import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "4c9bd8239ccb6f916ec6e71758f57302"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def buscar():
    WIKIPEDIA = "https://es.wikipedia.org/api/rest_v1/page/summary/{ciudad}"
    
    ciudad = entrada.get().strip()
    
    
    if not ciudad:
        messagebox.showwarning("Aviso", "Escribe una ciudad")
        return


    params = {
        "q": ciudad,
        "units": "metric",
        "appid": API_KEY,
        "lang": "es"
    }

    try:
        # 🌤️ Clima (OpenWeather)
        respuesta = requests.get(BASE_URL, params=params, timeout=10)
        data = respuesta.json()

        if data.get("cod") != 200:
            resultado.config(text="Error Clima: " + str(data.get("message")))
            return

        # 📚 Wikipedia (Ejercicio 1)
        # Usamos .title() para asegurar que 'puebla' sea 'Puebla' [cite: 5]
        ciudad_wiki = ciudad.title().replace(" ", "_")
        
        # Agregamos un 'User-Agent' para que Wikipedia nos deje entrar
        cabeceras = {'User-Agent': 'PracticaWebServices/1.0 (estudiante@ejemplo.com)'}
        
        # Consultamos el endpoint solicitado 
        respuesta_wikipedia = requests.get(WIKIPEDIA.format(ciudad=ciudad_wiki), headers=cabeceras, timeout=10)

        if respuesta_wikipedia.status_code == 200:
            datos_wiki = respuesta_wikipedia.json()

            # 📊 Mostramos el resultado usando las llaves directas [cite: 9, 10, 11, 12]
            resultado.config(
                text=f"Ciudad: {data['name']}\n"
                     f"Temperatura: {data['main']['temp']} °C\n"
                     f"Clima: {data['weather'][0]['description']}\n\n"
                     f"--- Wikipedia ---\n"
                     f"Título: {datos_wiki['title']}\n"
                     f"Descripción: {datos_wiki['extract']}\n"
                     f"Enlace: {datos_wiki['content_urls']['desktop']['page']}"
            )
        else:
            # Si Wikipedia devuelve algo distinto a 200, mostramos este aviso
            resultado.config(text=f"Clima OK, pero Wikipedia falló (Status: {respuesta_wikipedia.status_code})")

    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {str(e)}")

# 🖥️ Interfaz
ventana = tk.Tk()
ventana.title("Consulta de Clima")

tk.Label(ventana, text="Ciudad:").pack(pady=5)

entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

tk.Button(ventana, text="Consultar", command=buscar).pack(pady=10)

resultado = tk.Label(ventana, text="", justify="left", wraplength=400)
resultado.pack(pady=10)

ventana.mainloop()