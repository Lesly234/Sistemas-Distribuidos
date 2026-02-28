
#include <stdio.h>
#include <stdlib.h>
#include <winsock2.h>
#include <ws2tcpip.h>

#pragma comment(lib, "ws2_32.lib")

#define PORT 6000

int main() {
    WSADATA wsa;
    SOCKET server_fd, client_fd;
    struct sockaddr_in server, client;
    int c, num, recibido;

    // Inicializar Winsock
    if (WSAStartup(MAKEWORD(2,2), &wsa) != 0) {
        printf("Error en WSAStartup\n");
        return 1;
    }

    // Crear socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        printf("Error en socket\n");
        WSACleanup();
        return 1;
    }

    // Configurar dirección del servidor
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(PORT);

    // Enlazar
    if (bind(server_fd, (struct sockaddr *)&server, sizeof(server)) == SOCKET_ERROR) {
        printf("Error en bind\n");
        closesocket(server_fd);
        WSACleanup();
        return 1;
    }

    // Escuchar
    listen(server_fd, 3);
    printf("Servidor escuchando en puerto %d...\n", PORT);

    // Aceptar conexión
    c = sizeof(struct sockaddr_in);
    client_fd = accept(server_fd, (struct sockaddr *)&client, &c);
    if (client_fd == INVALID_SOCKET) {
        printf("Error en accept\n");
        closesocket(server_fd);
        WSACleanup();
        return 1;
    }
    printf("Cliente conectado!\n");

    while (1) {
        recibido = recv(client_fd, (char*)&num, sizeof(num), 0);
        if (recibido <= 0) break;

        num = ntohl(num);  // convertir de orden de red a host
        printf("Recibido: %d\n", num);

        if (num == 0) break;

        num++;
        num = htonl(num);  // convertir a orden de red
        send(client_fd, (char*)&num, sizeof(num), 0);
    }

    closesocket(client_fd);
    closesocket(server_fd);
    WSACleanup();
    printf("Servidor terminado.\n");
    return 0;
}

