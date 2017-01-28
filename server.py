#!/usr/bin/python
import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 1337


def main():
    server_socket = init_socket(SERVER_ADDRESS, SERVER_PORT)
    wait_and_print(server_socket)
    server_socket.close()


def init_socket(address, port):
    server_socket = socket.socket()
    server_socket.bind((address, port))
    server_socket.listen(1)

    return server_socket


def wait_and_print(server_socket):
    data = ""
    while data.lower() not in ["exit", "quit"]:
        (client_socket, client_address) = server_socket.accept()
        data = client_socket.recv(1337)
        print data

        client_socket.close()


if __name__ == "__main__":
    main()