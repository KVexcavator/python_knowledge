# глобальная блокировка интерпретатора в запросах отключается
import time
import threading
import requests

def read_example() -> None:
  response = requests.get('https://www.example.com')
  print(response.status_code)

sync_start = time.time()

read_example()
read_example()

sync_end = time.time()

print(f'Синхронное выполнение заняло{sync_end - sync_start:.4f} с.')
# 1.8187

thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

thread_start = time.time()

thread_1.start()
thread_2.start()

print('Все потоки работают!')

thread_1.join()
thread_2.join()

thread_end = time.time()

print(f'Многопоточное выполнение заняло {thread_end - thread_start:.4f} с.')
# 0.2772