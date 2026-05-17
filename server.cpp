#include <iostream>
#include <fstream>
#include <winsock2.h>

#pragma comment(lib, "ws2_32.lib")

using namespace std;

int main() {
    WSADATA wsa;
    SOCKET server, client;
    sockaddr_in serverAddr, clientAddr;
    int clientSize = sizeof(clientAddr);

    WSAStartup(MAKEWORD(2,2), &wsa);

    server = socket(AF_INET, SOCK_STREAM, 0);

    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(55000);
    serverAddr.sin_addr.s_addr = INADDR_ANY;

    bind(server, (sockaddr*)&serverAddr, sizeof(serverAddr));
    listen(server, 5);

    cout << "[+] SERVER STARTED..." << endl;

    while (true) {
        client = accept(server, (sockaddr*)&clientAddr, &clientSize);

        char buffer[1024] = {0};
        recv(client, buffer, sizeof(buffer), 0);

        cout << "[DATA] " << buffer << endl;

        ofstream log("log.txt", ios::app);
        log << buffer << endl;
        log.close();

        send(client, "LOG SAVED", 9, 0);

        closesocket(client);
    }

    closesocket(server);
    WSACleanup();

    return 0;
}