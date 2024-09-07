import socket

HEADER = 64
PORT = 5050
DISCONNECT_MSG = "![DISCONNECT]"
FORMATE = "utf-8"
SERVER = "192.168.1.108"
ADDR = (SERVER, PORT)

def create_client():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(ADDR)
        return client
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return None

def send(client, msg):
    try:
        message = msg.encode(FORMATE)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMATE)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
    except Exception as e:
        print(f"Error sending message: {e}")

def main():
    client = create_client()
    if client is None:
        return

    try:
        send(client, "hello")
        input()
        send(client, "hello world!")
        input()
        send(client, "okk...")
        input()
        send(client, DISCONNECT_MSG)
    finally:
        client.close()

if __name__ == "__main__":
    main()
