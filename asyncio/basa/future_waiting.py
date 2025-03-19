from asyncio import Future
import asyncio

# Создать задачу, которая асинхронно установит значение future
def make_request() -> Future:
  future = Future()
  asyncio.create_task(set_future_value(future))
  return future

# Ждать 1 с, прежде чем установить значение
async def set_future_value(future) -> None:
  await asyncio.sleep(1)
  future.set_result(42)

async def main():
  future = make_request()
  print(f'Будущий объект готов? {future.done()}')
  # False
  # Приостановить main, пока значение future не установлено
  value = await future
  print(f'Будущий объект готов? {future.done()}')
  # True
  print(value)
  # 42

asyncio.run(main())