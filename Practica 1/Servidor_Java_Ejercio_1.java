package sd_practica1_tarea;

import java.io.*;
import java.net.*;

public class Servidor_Java_Ejercio_1 {
    public static void main(String[] args) {
        int puerto = 5000; // Puerto de escucha

        try (ServerSocket servidor = new ServerSocket(puerto)) {
            System.out.println("Servidor escuchando en el puerto " + puerto);

            Socket socket = servidor.accept();
            System.out.println("Cliente conectado");

            BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter salida = new PrintWriter(socket.getOutputStream(), true);

            String mensaje = entrada.readLine();
            System.out.println("Cliente dijo: " + mensaje);

            // Respuesta
            salida.println("Hola que tal");

            socket.close();
            System.out.println("Servidor terminado.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
