import socket

HEADER = 64
SERVER = "192.168.56.1"
PORT = 5050
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode()
    msg_length = len(message)
    send_length = str(msg_length).encode()
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode())

print("Type 'q' if you want to exit.")
while True:
    message = input("Please enter your message: ")
    send(message)
    if message == 'q' or 'quit':
        break

send(DISCONNECT_MESSAGE)
