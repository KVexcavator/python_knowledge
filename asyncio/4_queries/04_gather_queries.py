# Конкурентное выполнение запросов с по­мощью gather
import asyncio
import aiohttp
from aiohttp import ClientSession
import sys
sys.path.append('..')
from util import fetch_status
from util import async_timed

@async_timed()
async def main():
  async with aiohttp.ClientSession() as session:
    urls = ['https://example.com' for _ in range(1000)]
    # енерировать список сопрограмм для каждого запроса
    requests = [fetch_status(session, url) for url in urls]
    # ждать завершения всех запросов
    status_codes = await asyncio.gather(*requests)
    print(status_codes)

asyncio.run(main())