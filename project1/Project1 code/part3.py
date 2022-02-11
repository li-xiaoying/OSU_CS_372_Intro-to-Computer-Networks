#!/usr/bin/env python3

"""
CS372 Project: Sockets and HTTP
Part3: The world’s simplest HTTP server
Author: Xiaoying Li
"""

# Refer to https://docs.python.org/3/howto/sockets.html
# Refer to https://realpython.com/python-sockets/
# Refer to https://emalsha.wordpress.com/2016/11/22/how-create-http-server-using-python-socket/
# Refer to https://www.oreilly.com/library/view/python-standard-library/0596000960/ch07s03.html

import socket
import select

# A random port number > 1023
port = 1234
# Create an INET, STREAMing socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to a localhost, and a random port number > 1023
server_socket.bind(('127.0.0.1', port))
# Html data to be sent
data = "HTTP/1.1 200 OK\r\n" \
       "Content-Type: text/html; charset=UTF-8\r\n\r\n" \
       "<html>Congratulations! You've downloaded the first Wireshark lab " \
       "file!</html>\r\n"
# Become a server socket and start listening request
server_socket.listen(1)
print("Connected by ('127.0.0.1', %d)" % port)
# Accept request and return socket connection and client socket address
(connection_socket, address) = server_socket.accept()

while True:
    # Using select module to check whether the socket is in a readable state
    is_readable = [server_socket]
    is_writable = []
    is_error = []
    r, w, e = select.select(is_readable, is_writable, is_error, 1.0)

    # If socket is ready for reading
    if r:
        # Accept request and return socket connection and client socket address
        (connection_socket, address) = server_socket.accept()
        # Get detailed data and print
        received_data = connection_socket.recv(1024).decode('utf-8')
        print("Received: {}".format(str(received_data)))
        send_data = data
        connection_socket.send(send_data.encode())
        print("Sending>>>>>>>>>>")
        print(data)
        print("<<<<<<<<<<<<<<<<<")
        connection_socket.close()

    # If socket is not ready for reading, break the program
    else:
        break
