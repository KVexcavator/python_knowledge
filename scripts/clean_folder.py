# очистка папки
import os
import time

FOLDER = os.path.expanduser("~/Pictures")  # Путь к папке "Изображения"
EXTENSIONS = (".png", ".jpg", ".jpeg")
DAYS = 5  # Удалять скрины старше 5 дней

now = time.time()

for filename in os.listdir(FOLDER):
    if filename.lower().endswith(EXTENSIONS) and "screenshot" in filename.lower():
        filepath = os.path.join(FOLDER, filename)
        file_age = now - os.path.getmtime(filepath)
        if file_age > DAYS * 86400:
            os.remove(filepath)
            print(f"Удалён: {filename}")
