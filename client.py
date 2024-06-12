#! /usr/bin/env python3

import socket, sys, re, time

def read_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

def frame_and_send_file(connection, filename):
    file_data = read_file(filename)
    connection.sendall(filename.encode())
    time.sleep(1)
    connection.sendall(file_data)
    time.sleep(1)
    connection.sendall(b'EOF')

def deframe_ack(connection):
    ack_data = connection.recv(1024).decode()
    print(f"Acknowledgement received: {ack_data}")

def main():
    host = '127.0.0.1'
    port = 50000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host,port))

    filename = sys.argv[1]
    print(f"Sending file: {filename}")

    frame_and_send_file(client_socket, filename)
    print("File sent successfully")

    deframe_ack(client_socket)
    print("Closing connection.")

    client_socket.close()

if __name__ == "__main__":
    main()
