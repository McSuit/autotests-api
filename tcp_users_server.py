import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(10)
    
    messages = []
    
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Пользователь с адресом: {client_address} подключился к серверу")
            
            data = client_socket.recv(1024)
            if data:
                message = data.decode()
                print(f"Пользователь с адресом: {client_address} отправил сообщение: {message}")
                messages.append(message)
                
                response = '\n'.join(messages)
                client_socket.send(response.encode())
            
            client_socket.close()
    except KeyboardInterrupt:
        server_socket.close()

if __name__ == '__main__':
    start_server()
