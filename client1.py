import socket

# set up socket connection
HOST = '0.0.0.0'
PORT = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    # accept incoming client connection
    conn, addr = s.accept()
    print('Connected by', addr)

    # send file data and checksum to client
    conn.sendall(client_data)

    # close connection
    conn.close()