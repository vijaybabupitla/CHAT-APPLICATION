import socket

def server_program():
    server_socket = socket.socket()
    host = socket.gethostname()
    port = 5000
    print(host)
    server_socket.bind((host, port))
    
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print(f"Connection from {address}")
    
    while True:
        message = conn.recv(1024).decode()
        if message.lower() == "bye":
            print("Chat ended.")
            break
        print(f"Client: {message}")
        message = input("Server: ")
        conn.send(message.encode())
        if message.lower() == "bye":
            print("Chat ended.")
            break
    
    conn.close()

server_program()
