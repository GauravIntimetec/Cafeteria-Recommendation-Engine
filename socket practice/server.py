import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Received message: {message.decode()}")
            else:
                break
        except:
            break
    client_socket.close()
    clients.remove(client_socket)

def send_notification(message):
    for client in clients:
        try:
            client.sendall(message.encode())
        except:
            client.close()
            clients.remove(client)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)
    print("Server listening on port 12345")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    while True:
        notification = input("Enter notification to send to all clients: ")
        send_notification(notification)


