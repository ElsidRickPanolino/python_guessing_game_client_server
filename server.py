import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(5)
print('Server listening on port 12345...')

max = 100

while True:
    client_socket, client_address = server_socket.accept()
    print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))
    

    random_int = random.randint(1,max)

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        decoded = data.decode()
        if decoded == "close":
            client_socket.close()
            print("Client closed")
            break

        if decoded.isdigit():
            guess = int(decoded)
            print()
            print(f"Guess: {guess}")

            if guess == random_int:
                print("guess is correct")
                response = "Correct! You guessed the number. New random number is generated"
                random_int = random.randint(1,max)
            elif guess < random_int:
                print("guess is low")
                response = "Higher"
            else:
                print("guess is high")
                response = "Lower"

        else:
            response = "invalid input"
                
        client_socket.send(response.encode())
    
    client_socket.close()
    break

server_socket.close()
print("Server closed")