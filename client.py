import socket

client_socket = socket.socket()

client_socket.connect(('localhost', 1000))

user_name = input('Enter your name ')
client_socket.send(bytes(user_name, 'utf-8'))

print(client_socket.recv(1024).decode())
