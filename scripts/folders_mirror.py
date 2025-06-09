# Синхронизация папок в реальном времени (односторонняя) 

import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

SOURCE = "source_folder"
TARGET = "target_folder"

os.makedirs(SOURCE, exist_ok=True)
os.makedirs(TARGET, exist_ok=True)

class SyncHandler(FileSystemEventHandler):
  def on_any_event(self, event):
    rel_path = os.path.relpath(event.src_path, SOURCE)
    target_path = os.path.join(TARGET, rel_path)

    if event.is_directory:
      if event.event_type == "created" and not os.path.exists(target_path):
        os.makedirs(target_path, exist_ok=True)
    else:
      if event.event_type in ("created", "modified"):
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        shutil.copy2(event.src_path, target_path)
        print(f"Скопировано: {rel_path}")
      elif event.event_type == "deleted":
        if os.path.exists(target_path):
          os.remove(target_path)
          print(f"Удалено: {rel_path}")

observer = Observer()
observer.schedule(SyncHandler(), path=SOURCE, recursive=True)
observer.start()

print(f"Слежение за {SOURCE} → {TARGET}")
try:
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  observer.stop()
observer.join()
