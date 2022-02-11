"""
CS372 Project: Client-Server Chat
Author: Xiaoying Li
Client:
1. The client creates a socket and connects to ‘localhost’ and port xxxx
2. When connected, the client prompts for a message to send
3. If the message is /q, the client quits
4. Otherwise, the client sends the message
5. The client calls recv to receive data
6. The client prints the data
7. Back to step 2
8. Sockets are closed (can use with in python3)
"""

# Adapted from
# https://www.journaldev.com/15906/python-socket-programming-server-client


import socket


def client_program():
    # set the hostname and port number same as the server
    host = '127.0.0.1'  # localhost
    port = 2345  # random port number > 1023

    # create a socket instance
    client_socket = socket.socket()
    # connect the socket to the server
    client_socket.connect((host, port))

    print("Connected to: localhost on port: " + str(port))
    print("Type /q to quit")
    print("Enter message to send...")
    # prompt for a message to send and take input
    message = input(">")
    message = message + "\nType /q to quit\nEnter message to send..."

    # loop as long as the input message is not /q
    # if the input message is /q, the client quits
    while message != '/q':
        # send message
        client_socket.send(message.encode())
        # receive response
        data = client_socket.recv(4096).decode()

        # if the received data is /q, the client quits
        if data == '/q':
            break

        print(data)
        # again prompt for a reply and take input
        message = input(">")

    # close the connection
    client_socket.close()


if __name__ == '__main__':
    client_program()
