#!/usr/bin/env python3

"""
CS372 Project: Sockets and HTTP
Part1: Using a socket to GET a file
Author: Xiaoying Li
"""

# Adapted from https://zetcode.com/python/socket/ "Python Socket GET request"

import socket

# Create an INET, STREAMing socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the web server on port 80 - the normal http port
    s.connect(("gaia.cs.umass.edu", 80))
    # Send the GET request to read the page
    s.sendall(b"GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\n"
              b"Host:gaia.cs.umass.edu\r\n\r\n")

    # Use a while loop to process the received data and print data
    while True:
        data = s.recv(1024)
        if not data:
            break
        print("Request: GET /wireshark-labs/INTRO-wireshark-file1.html "
              "HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n")
        print("[RECV] - length: %d" % (len(data)))
        print(data.decode())
