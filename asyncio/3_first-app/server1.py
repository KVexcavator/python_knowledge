# это блокирующий сервер, после подключения будет сообщение о закрытии
import socket

# создать TCP-сервер
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# задать адресс сокета
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)
# слушать запросы на подключение
server_socket.listen()

# дождаться подключения и выделить клиенту почтовый ящик
connection, client_address = server_socket.accept()
print(f"Получен запрос на подключение от {client_address}!")
# уже можно подключиться из другого терминала
# telnet localhost 8000
