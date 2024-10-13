import socket

def client_program():
    client_socket = socket.socket()
    host = socket.gethostname()
    port = 5000
    
    client_socket.connect((host, port))
    
    while True:
        message = input("Client: ")
        client_socket.send(message.encode())
        if message.lower() == "bye":
            print("Chat ended.")
            break
        data = client_socket.recv(1024).decode()
        print(f"Server: {data}")
        if data.lower() == "bye":
            print("Chat ended.")
            break
    
    client_socket.close()

client_program()
