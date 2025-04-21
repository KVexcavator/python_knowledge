# Отправка веб-запроса с по­мощью aiohttp
import asyncio
import aiohttp
from aiohttp import ClientSession

async def fetch_status(session: ClientSession, url: str) -> int:
  timeout = aiohttp.ClientTimeout(total=2.0)
  async with session.get(url, timeout=timeout) as response:
    return response.status

async def main():
  session_timeout = aiohttp.ClientTimeout(total=3.0, connect=1.0)
  async with ClientSession(timeout=session_timeout) as session:
    try:
      status = await fetch_status(session, 'https://example.com')
      print(f"Status: {status}")
    except asyncio.TimeoutError:
      print("Request timed out")
