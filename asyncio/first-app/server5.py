# Асинхронный эхо-сервер
# Имеется одна сопрограмма, listen_for_connection, прослушивающая порт. Как только клиент подключился, она запускает задачу echo для этого клиента, которая ожидает поступления данных и отправляет их обратно клиенту.
import asyncio
import socket
from asyncio import AbstractEventLoop

async def echo(connection: socket, loop: AbstractEventLoop) -> None:
  # В бесконечном цикле ожидаем данных от клиента
  while data := await loop.sock_recv(connection, 1024):
    # Получив данные, отправляем их обратно клиенту
    await loop.sock_sendall(connection, data)

async def listen_for_connection(server_socket: socket, loop: AbstractEventLoop):
  while True:
    connection, address = await loop.sock_accept(server_socket)
    connection.setblocking(False)
    print(f"Получен запрос на подключение от {address}!")
    # После получения запроса на подключение создаем задачу echo, ожидающую данные от клиента
    asyncio.create_task(echo(connection, loop))

async def main():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  server_address = ('127.0.0.1', 8000)
  server_socket.setblocking(False)
  server_socket.bind(server_address)
  server_socket.listen()

  # Запускаем сопрограмму прослушивания порта на предмет подключений
  await listen_for_connection(server_socket, asyncio.get_event_loop())
  
asyncio.run(main())

# Сопрограмма, прослушивающая порт, запускает по одной задаче для каждого нового подключения
# telnet localhost 8000