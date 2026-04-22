import requests

URL_BASE = "http://127.0.0.1:5000"

def Pagar(numero_tarjeta, monto, nombre, codigo_CVV):
    payload = {
        "numero_tarjeta": numero_tarjeta,
        "monto": monto,
        "nombre": nombre,
        "codigo_CVV": codigo_CVV
    }
    try:
        respuesta = requests.post(f"{URL_BASE}/pagar", json=payload)
        resultado = respuesta.json().get("resultado", False)
        
        if resultado:
            print("TRANSACCIÓN EXITOSA")
        else:
            print("FALLÓ LA TRANSACCIÓN")
            
        return resultado
    except Exception as e:
        print("Error de conexión:", e)
        return False

def Comprar(id_producto, precio, numero_productos, total):
    payload = {
        "id_producto": id_producto,
        "precio": precio,
        "numero_productos": numero_productos,
        "total": total
    }
    try:
        respuesta = requests.post(f"{URL_BASE}/comprar", json=payload)
        resultado = respuesta.json().get("resultado", False)
        
        if resultado:
            print("COMPRA EXITOSA")
        else:
            print("FALLÓ LA COMPRA")
            
        return resultado
    except Exception as e:
        print("Error de conexión:", e)
        return False

if __name__ == "__main__":
    print("---SERVICIOS WEB DE COMPRA---\n")
    
    print("1. Ejecutando Pagar(123456789, 1000, 'Juan Perez', 456):")
    Pagar(123456789, 1000, "Juan Perez", 456)
    
    print("\n2. Ejecutando Comprar(101, 250, 4, 1000):")
    Comprar(101, 250, 4, 1000)
    
    print("\n--- Lesly y Arantza ---")