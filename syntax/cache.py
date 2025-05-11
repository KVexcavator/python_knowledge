# кеширование детерминированных функций
# таблетка от переполнения памяти
# когда кеш заполнен, наименее используемые значения удаляются
from functools import lru_cache

@lru_cache(1024)
def function_to_cache(*args):
  ...

print(function_to_cache.cache_info().currsize)
print(function_to_cache.cache_info())