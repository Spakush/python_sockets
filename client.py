#!/usr/bin/python
import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 1337


def main():
    client_socket = init_socket(SERVER_ADDRESS, SERVER_PORT)
    send_data(client_socket)


def init_socket(con_add, con_port):
    client_socket = socket.socket()
    client_socket.connect((con_add, con_port))

    return client_socket


def send_data(client_socket):
    data = raw_input("Enter message here: ")
    client_socket.send(data)

    client_socket.close()


if __name__ == "__main__":
    main()