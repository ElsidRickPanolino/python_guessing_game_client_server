import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    guess = input("Enter your guess (or 'close' to exit): ")

    if guess == "close":
        client_socket.send(guess.encode())
        break

    client_socket.send(guess.encode())
    response = client_socket.recv(1024)
    decoded = response.decode()
    print(decoded)

client_socket.close()