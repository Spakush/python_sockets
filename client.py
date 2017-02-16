#!/usr/bin/python
import socket
import argparse

SERVER_ADDRESS = "0.0.0.0"
SERVER_PORT = 1337

def main(username, password):
    client_socket = init_socket(SERVER_ADDRESS, SERVER_PORT)
    print "will send args"
    client_socket.send("{} {}".format(username, password))
    print "args sent"
    connection_conf(client_socket)
    client_socket.close()


def init_socket(con_add, con_port):
    client_socket = socket.socket()
    client_socket.connect((con_add, con_port))

    return client_socket


def connection_conf(client_socket):
    print "waiting for msg"
    num = client_socket.recv(1337)
    if isinstance(int(num), int) and num != '0':
        print "i'm client number {}".format(num)
        send_data(client_socket)
    else:
        print "wrong arguments, can't connect"
        print "dissconnecting"
        

def send_data(client_socket):
    print "####################"
    print "Enter message here: "
    print "####################"
    data = raw_input()
    client_socket.send(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("username", type = str)
    parser.add_argument("password", type = str)
    args = parser.parse_args()

    main(args.username, args.password)