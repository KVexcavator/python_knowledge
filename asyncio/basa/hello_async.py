import asyncio

async def my_coroutine() -> None:
  print('Hello world!')

async def coroutine_add_one(number: int) -> int:
  return number + 1

# сопрограммы не выполняются, если их вызвать напрямую
# возвращается объект сопрограммы, который будет выполнен позже


asyncio.run(my_coroutine())

result = asyncio.run(coroutine_add_one(1))
print(result)