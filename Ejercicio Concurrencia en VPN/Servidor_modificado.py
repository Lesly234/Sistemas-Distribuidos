import socket

host = '0.0.0.0'  # Escuchar en todas las interfaces
port = 12345        # Puerto de escucha

# Configura el socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
# listen(5) significa que puede tener hasta 5 clientes en fila de espera
server_socket.listen(5) 
print(f"Servidor iniciado. Esperando conexiones en el puerto {port}...")

# Agregamos el ciclo infinito para que el servidor no se cierre
while True:
    # Acepta la conexión de un cliente
    conn, addr = server_socket.accept()
    client_ip = addr[0]  
    print(f"\n--- Nueva conexión desde: {addr} ---")

    # Define el nombre del archivo con la IP del cliente
    file_name = f"archivo_recibido_{client_ip.replace('.', '_')}.mp4"  
    print(f"Guardando archivo como: {file_name}")

    # Recibe y guarda el archivo
    with open(file_name, "wb") as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    conn.close()
    print(f"Archivo de {client_ip} recibido y guardado correctamente.")
    print("Esperando al siguiente cliente...")