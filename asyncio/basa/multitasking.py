import asyncio
import sys
sys.path.append('..')
from util import delay

async def hello_every_second():
  for i in range(2):
    await asyncio.sleep(1)
    print("пока я жду, исполняется другой код!")

async def main():
  sleep_for_three = asyncio.create_task(delay(3))
  sleep_again = asyncio.create_task(delay(3))
  sleep_once_more = asyncio.create_task(delay(3))

  await hello_every_second()

  await sleep_for_three
  await sleep_again
  await sleep_once_more

asyncio.run(main())