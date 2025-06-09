# Тайм-ауты в сочетании с as_completed
# управляет временем работы as_completed; если потребуется больше, то каждый допускающий ожидание объект в итераторе возбудит исключение TimeoutException в точке ожидания с по­мощью await
# Пример: Два запроса по 10 с и один запрос, занимающий 1 с., тайм-аут 2 с при вызове as_completed. По завершении цикла печатает все выполняемые в данный момент задачи
import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
sys.path.append('..')
from util import async_timed
from util import fetch_delay_and_status

@async_timed()
async def main():
  async with aiohttp.ClientSession() as session:
    fetchers = [
      fetch_delay_and_status(session, 'https://example.com', 1),
      fetch_delay_and_status(session, 'https://example.com', 10),
      fetch_delay_and_status(session, 'https://example.com', 10)
    ]
    for done_task in asyncio.as_completed(fetchers, timeout=2):
      try:
        result = await done_task
        print(result)
      except asyncio.TimeoutError:
        print('Произошел тайм-аут!')
    for task in asyncio.tasks.all_tasks():
      print(task)

asyncio.run(main())