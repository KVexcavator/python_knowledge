# as_completed принимает список допускающих ожидание объектов и возвращает итератор по будущим объектам
# один запрос завершается быстро, а другой медленно? результат обрабатывается по мере доступности

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
         fetch_delay_and_status(session, 'https://www.example.com', 1),
         fetch_delay_and_status(session, 'https://www.example.com', 1),
         fetch_delay_and_status(session, 'https://www.example.com', 10)
      ]
      for finished_task in asyncio.as_completed(fetchers):
        print(await finished_task)

asyncio.run(main())