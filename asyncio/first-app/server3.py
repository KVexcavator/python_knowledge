#  Разрешение нескольких подключений
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8001)
server_socket.bind(server_address)
server_socket.listen()
# пометить серверный сокет как не блокирующий
server_socket.setblocking(False)

connections = []

try:
  while True:
    try:
      connection, client_address = server_socket.accept()
      # пометить серверный сокет как не блокирующий
      connection.setblocking(False)
      print(f"Получен запрос на подключение от {client_address}!")
      connections.append(connection)
    except BlockingIOError:
      pass

    for connection in connections:
      try:
        buffer = b''

        while buffer[-2:] != b'\r\n':
          data = connection.recv(2)
          if not data:
            break
          else:
            print(f"Получены данные: {data}!")
            buffer = buffer + data

        print(f"Все данные: {buffer}!")
        connection.send(buffer)
      except BlockingIOError:
        pass
finally:
  server_socket.close()

# telnet localhost 8001
#  При использовании блокирующих сокетов клиент 1 подключается, но клиент 2 заблокирован, пока первый клиент не отправит данные
# для решения посечаем клиент и сервер как неблокируюище и перехватываем исключения в цикле
# это будет работать но за дорого
# Из-за перехвата исключений в бесконечном цикле потребление процессора быстро доходит до 100 % и на этом уровне остается
