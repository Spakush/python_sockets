#!/usr/bin/python
import socket

SERVER_ADDRESS = "0.0.0.0"
SERVER_PORT = 1337


def main():
    client_socket = init_socket(SERVER_ADDRESS, SERVER_PORT)
    get_num(client_socket)
    send_data(client_socket)


def init_socket(con_add, con_port):
    client_socket = socket.socket()
    client_socket.connect((con_add, con_port))

    return client_socket

def get_num(client_socket):
    num = client_socket.recv(1337)
    print "im client number {}".format(num)

def send_data(client_socket):
    print "####################"
    print "Enter message here: "
    print "####################"
    data = raw_input()
    client_socket.send(data)

    client_socket.close()


if __name__ == "__main__":
    main()