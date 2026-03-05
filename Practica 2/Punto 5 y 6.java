package client;

import server.EchoObject; 
import java.io.*;

public class Echo {
    public static void main(String[] args) {
        // Para los puntos 5 y 6, creamos el objeto real directamente (sin Stub)
        EchoObject objetoReal = new EchoObject(); 
        
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String cadena;

        try {
       
            System.out.println("MODO LOCAL (Sin Sockets). Escribe algo:");
            
            while (true) {
                System.out.print("Local> ");
                cadena = in.readLine();
                
                if (cadena == null || cadena.equalsIgnoreCase("salir")) break;

                String respuesta = objetoReal.echo(cadena); 
                System.out.println(respuesta);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}