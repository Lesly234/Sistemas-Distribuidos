package sd_practica1_tarea.cliente;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Cliente_Java_Ejercicio_2  {
    public static void main(String[] args) {
        String host = "192.168.87.5"; // localhost
        int puerto = 6000;

        try (Socket socket = new Socket(host, puerto);
             DataOutputStream salida = new DataOutputStream(socket.getOutputStream());
             DataInputStream entrada = new DataInputStream(socket.getInputStream());
             Scanner sc = new Scanner(System.in)) {

            int numero;

            do {
                System.out.print("Ingrese un numero (0 para salir): ");
                numero = sc.nextInt();

                // enviar entero en orden de red
                salida.writeInt(numero);
                salida.flush();

                if (numero != 0) {
                    int respuesta = entrada.readInt();
                    System.out.println("Servidor responde: " + respuesta);
                }

            } while (numero != 0);

            System.out.println("Cliente terminado.");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
