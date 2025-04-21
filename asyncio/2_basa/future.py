from asyncio import Future

my_future = Future()
print(f'my_future готов? {my_future.done()}')
# False
my_future.set_result(42)
print(f'my_future готов? {my_future.done()}')
# True
print(f'Какой результат хранится в my_future? {my_future.result()}')
# Какой результат хранится в my_future? 42