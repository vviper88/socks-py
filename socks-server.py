#!/usr/bin/env python3
import socket
import threading

def handle_client(client_socket, address):
    while True:
        data = client_socket.recv(1024)
        if data == "!DC".encode():
           client_socket.close()
           client_sockets.remove(client_socket) 

def send_all(message):
    for client_socket in client_sockets:
        client_socket.sendall(message.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 7777))
server.listen(4)

client_sockets = []

print("Server is up and listening for connections.")

try:
    while True:
        client_socket, address = server.accept()
        client_sockets.append(client_socket)
        
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()
        send_all("New client connected.")
except KeyboardInterrupt:
    print("Closing...")
    server.close()