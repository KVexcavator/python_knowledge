# это просто подсказка, код запустится
def odd(n: int) -> bool:
  return n % 2 !=0

def main():
  print(odd("hello, world!"))

# используется для того, чтобы код выполнялся только при запуске скрипта напрямую, а не при его импорте в другой модуль
if __name__ == "__main__":
  main()

# mypy даёт развернутую подсказку
# python -m pip install mypy
# mypy --strict type_hints.py 
# получим подробное описание ошибок с подсказками