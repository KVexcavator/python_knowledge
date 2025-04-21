# Отправка веб-запроса с по­мощью aiohttp
import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
sys.path.append('..')
from util import async_timed

@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
  async with session.get(url) as result:
    return result.status

@async_timed()
async def main():
  # создание клиенского сеанса
  async with aiohttp.ClientSession() as session:
    url = 'https://www.example.com'
    # отправка запроса
    status = await fetch_status(session, url)
    print(f'Состояние для {url} было равно {status}')

asyncio.run(main())
