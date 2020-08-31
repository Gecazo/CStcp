import socket

sock: socket = socket.socket()
print('Socket created')

sock.bind(('localhost', 1000))

sock.listen(3)
print('Waiting for connections')

while True:
    client_socket, address = sock.accept()
    user_name = client_socket.recv(1024).decode()
    print('Connected with ', address, user_name)

    client_socket.send(bytes("Connected",'utf-8'))
    client_socket.close()
