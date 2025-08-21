import socket


message_list = ["Привет, сервер!", "Как дела?"]

# Отправляем сообщение серверу
for message in message_list:

    # Создаем TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключаемся к серверу
    server_address = ("localhost", 12345)
    client_socket.connect(server_address)
    client_socket.send(message.encode())

    # Получаем ответ от сервера
    response = client_socket.recv(1024).decode()
    print(response)

    # Закрываем соединение
    client_socket.close()
