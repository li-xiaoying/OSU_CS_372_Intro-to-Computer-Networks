"""
CS372 Project: Client-Server Chat
Author: Xiaoying Li
Server:
1. The server creates a socket and binds to ‘localhost’ and port xxxx
2. The server then listens for a connection
3. When connected, the server calls recv to receive data
4. The server prints the data, then prompts for a reply
5. If the reply is /q, the server quits
6. Otherwise, the server sends the reply
7. Back to step 3
8. Sockets are closed (can use with in python3)
"""

# Adapted from
# https://www.journaldev.com/15906/python-socket-programming-server-client


import socket


def server_program():
    # set the hostname and port number
    host = '127.0.0.1'  # localhost
    port = 2345  # random port number > 1023

    # create a socket instance
    server_socket = socket.socket()
    # bind the socket to host address and port number
    server_socket.bind((host, port))
    # become a server socket and start listening request
    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    # accept new connection
    # return socket connection and client socket address
    conn, address = server_socket.accept()

    print("Server listening on: localhost on port: " + str(port))
    print("Connected by " + str(address))
    print("Waiting for message...")

    while True:
        # receive data stream
        data = conn.recv(4096).decode()

        # if data is not received, the server quits
        if not data:
            break

        # if the received data is /q, the server quits
        if data == '/q':
            break

        print(str(data))
        # prompt for a reply and take input
        data = input('>')
        # send reply to the client
        conn.send(data.encode())

        # if the input reply is /q, the server quits
        if data == '/q':
            break

    # close the connection
    conn.close()


if __name__ == '__main__':
    server_program()
