#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib") // Librería de Winsock

#define PORT 5000
#define SERVER_IP "192.168.87.5"

int main() {
    WSADATA wsa;
    SOCKET sock;
    struct sockaddr_in server;
    char buffer[1024] = "";
    char respuesta[1024];
    int len;

    // Inicializar Winsock
    if (WSAStartup(MAKEWORD(2,2), &wsa) != 0) {
        printf("Error en WSAStartup\n");
        return 1;
    }

    // Crear socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        printf("Error en socket\n");
        WSACleanup();
        return 1;
    }

    server.sin_family = AF_INET;
    server.sin_port = htons(PORT);
    server.sin_addr.s_addr = inet_addr(SERVER_IP);

    // Conectar al servidor
    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        printf("Error en connect\n");
        closesocket(sock);
        WSACleanup();
        return 1;
    }

    printf("Escribe un mensaje para el servidor: \n");
    fgets(buffer, sizeof(buffer), stdin);



    // Enviar mensaje
    send(sock, buffer, strlen(buffer), 0);


    // Recibir respuesta
    len = recv(sock, respuesta, sizeof(respuesta)-1, 0);
    if (len > 0) {
        respuesta[len] = '\0';
        printf("Servidor responde: %s\n", respuesta);
    }

    closesocket(sock);
    WSACleanup();
    return 0;
}

