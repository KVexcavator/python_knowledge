import asyncio

async def add_one(number: int) -> int:
  return number + 1

async def main() -> None:
  # Приостановить main до возврата из one_plus_one
  one_plus_one = await add_one(1)
  # Приостановить main до возврата из two_plus_one
  two_plus_one = await add_one(2)
  print(one_plus_one)
  print(two_plus_one)

asyncio.run(main())