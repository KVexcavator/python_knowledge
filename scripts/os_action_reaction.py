# Реакция на события ОС — автозапуск скриптов при изменении файлов, подключении дисков, появлении процессов
# Слежение за изменениями в проектах, синхронизация
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

WATCH_DIR = "watched"

class Handler(FileSystemEventHandler):
  def on_created(self, event):
    if not event.is_directory:
      print(f"Новый файл: {event.src_path}")
      # Пример: обработать файл или переместить
      # process_file(event.src_path)

  def on_modified(self, event):
    if not event.is_directory:
      print(f"Файл изменён: {event.src_path}")

  def on_deleted(self, event):
    if not event.is_directory:
      print(f"Файл удалён: {event.src_path}")

os.makedirs(WATCH_DIR, exist_ok=True)
observer = Observer()
observer.schedule(Handler(), WATCH_DIR, recursive=True)
observer.start()

print(f"🕵️ Слежение за: {WATCH_DIR}")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
