# Обработка исключений при использовании gather
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
    # есть не существующий адрес
    urls = ['https://example.com', 'python://example.com']
    tasks = [fetch_status(session, url) for url in urls]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    exceptions = [res for res in results if isinstance(res, Exception)]
    successful_results = [res for res in results if not isinstance(res, Exception)]

    print(f'Все результаты: {results}')
    print(f'Завершились успешно: {successful_results}')
    print(f'Завершились с исключением: {exceptions}')

asyncio.run(main())