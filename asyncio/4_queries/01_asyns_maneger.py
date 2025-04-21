# Асинхронный контекстный менеджер, ожидающий подключения клиента

import asyncio
import socket
from types import TracebackType
from typing import Optional, Type

class ConnectedSocket:

  def __init__(self, server_socket):
    self._connection = None
    self._server_socket = server_socket

  # вызывается при входе в блок with, ждетподключения клиента и возвращает это подключение
  async def __aenter__(self):
    print('Вход в контекстный менеджер, ожидание подключения')
    loop = asyncio.get_event_loop()
    connection, address = await loop.sock_accept(self._server_socket)
    self._connection = connection
    print('Подключение подтверждено')
    return self._connection
  
  # вызывается при выходе из блока with, производит очистку ресурса, в данном случае закрывается подключение
  async def __aexit__(
    self,
    exc_type: Optional[Type[BaseException]],
    exc_val: Optional[BaseException],
    exc_tb: Optional[TracebackType]
  ):
    print('Выход из контекстного менеджера')
    self._connection.close()
    print('Подключение закрыто')

async def main():
  loop = asyncio.get_event_loop()
  server_socket = socket.socket()
  server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server_address = ('127.0.0.1', 8003)
  server_socket.setblocking(False)
  server_socket.bind(server_address)
  server_socket.listen()
  # вызывается __aenter__ и начинается ожидание подключения
  async with ConnectedSocket(server_socket) as connection:
    data = await loop.sock_recv(connection, 1024)
    print(data)
    # под капотом здесь вызывается __aexit__ и подключение закрывается

asyncio.run(main())
# telnet localhost 8003