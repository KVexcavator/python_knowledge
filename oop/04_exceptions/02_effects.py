# NoReturn функция не должна возвращать значение
from typing import NoReturn

def never_returns() -> NoReturn:
  print("I am about to raise an exception")
  raise Exception("This is always raised")
  print("This line will never execute")
  return "I won't be returned"
# >>> never_returns()
# I am about to raise an exception
# Traceback (most recent call last):
# ...
# Exception: This is always raised

# если будем вызывать из другой функции без обработки ошибки, выполнение прекратится

def call_exceptor() -> None:
  print("call_exceptor starts here...")
  never_returns()
  print("an exception was raised...")
  print("...so these lines don't run")

# >>> call_exceptor()
# call_exceptor starts here...
# ...
# Exception: This is always raised

# вызов с обработкой ошибки поможет продолжить выполнение

def handler() -> None:
  try:
    never_returns()
    print("Never executed")
  except Exception as ex:
    print(f"I caught and exception: {ex!r}")
  print("Executed after the exception")

# I am about to raise an exception
# I caught an exception: Exception('This is always raised')
# Executed after the exception

# Если вдруг надо поймать конкретные виды ошибок
from typing import Union

def funny_division(divisor: float) -> Union[str, float]:
  try:
    return 100 / divisor
  except ZeroDivisionError:
    return "Zero in not a good idea!"
  
# print(funny_division(0))
# Zero is not a good idea!
# print(funny_division(50.0))
# 2.0
# print(funny_division("hello"))
# Traceback (most recent call last):
# ...
# TypeError: unsupported operand type(s) for /: 'int' and 'str'

# Вот пример, который вызывает три различных типа исключений.

def funnier_division(divisor: int) -> Union[str, float]:
  try:
    if divisor == 13:
      raise ValueError("13 is an unlucky number")
    return 100 / divisor
  except (ZeroDivisionError, TypeError):
    return "Enter a number other than zero"

for val in (0, "hello", 50.0, 13):
  print(f"Testing {val!r}:", end=" ")
  print(funnier_division(val))

# Testing 0: Enter a number other than zero
# Testing 'hello': Enter a number other than zero
# Testing 50.0: 2.0
# ...
# ValueError: 13 is an unlucky number

# если добавить к предыдуему примеру еще один вызов в конце, отработает только первыу вызов этого исключения
# except ValueError:
#   print("No, No, not 13!")
#   raise

