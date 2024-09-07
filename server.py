import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMATE = "utf-8"
DISCONNECT_MSG = "![DISCONNECT]"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMATE)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMATE)
                if msg == DISCONNECT_MSG:
                    print(f"[{addr}] Disconnected...")
                    connected = False
                print(f"[{addr}] {msg}")
        except Exception as e:
            print(f"[ERROR] An error occurred with {addr}: {e}")
            connected = False
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        try:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"\n[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        except Exception as e:
            print(f"[ERROR] An error occurred: {e}")

print("[STARTING] Server is starting...")
start()
