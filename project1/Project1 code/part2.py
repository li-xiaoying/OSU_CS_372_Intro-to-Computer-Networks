#!/usr/bin/env python3

"""
CS372 Project: Sockets and HTTP
Part2: GET the data for a large file
Author: Xiaoying Li
"""

# Adapted from https://zetcode.com/python/socket/ "Python Socket GET request"
# Refer to https://pythonprogramming.net/sockets-tutorial-python-3/

import socket

# Create an INET, STREAMing socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the web server on port 80 - the normal http port
    s.connect(("gaia.cs.umass.edu", 80))
    # Send the GET request to read the page
    s.sendall(b"GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\n"
              b"Host:gaia.cs.umass.edu\r\n\r\n")

    # Use a while loop to process the received data and print data
    while True:
        full_data = ""

        # Use a while loop to detect when recv return <= 0 byte
        while True:
            data = s.recv(2)
            if not data:
                break
            # Buffering through the full message
            full_data += data.decode("utf-8")

        # Print data
        if len(full_data) > 0:
            print("Request: GET /wireshark-labs/HTTP-wireshark-file3.html "
                  "HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n")
            print("[RECV] - length: %d" % (len(full_data)))
            print(full_data)

        # Close the connection when recv return <= 0 byte
        if not data:
            break
