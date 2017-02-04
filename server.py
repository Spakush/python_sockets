#!/usr/bin/python
import socket
import threading

SERVER_ADDRESS = "0.0.0.0"
SERVER_PORT = 1337
clients = 0

def main():
    read_clients()
    server_socket = init_socket(SERVER_ADDRESS, SERVER_PORT)
    wait_for_clients(server_socket)
    server_socket.close()


def init_socket(address, port):
    server_socket = socket.socket()
    server_socket.bind((address, port))
    server_socket.listen(10)

    return server_socket

def wait_for_clients(server_socket):
    global clients
    while True:
        (client_socket, client_address) = server_socket.accept()
        clients += 1
        save_clients_to_file()
        shlomi = threading.Thread(target=handle_client, args=(client_socket, ))
        shlomi.start()
        

def handle_client(client_socket):
    client_socket.send(str(clients))
    data = client_socket.recv(1337)
    print data
    client_socket.close()

def save_clients_to_file():
    with open("clients.txt", "w+") as f:
        f.write(str(clients))

def read_clients():
    global clients
    with open("clients.txt", "r") as f:
        clients = int(f.read(1337))

if __name__ == "__main__":
    main()