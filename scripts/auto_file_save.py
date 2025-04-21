# Автоматическое создание резервной копии файла
# Создаёт .bak-копию, если файл существует
import shutil
import os

file_path = "data.txt"
backup_path = f"{file_path}.bak"

if os.path.exists(file_path):
    shutil.copy(file_path, backup_path)
    print(f"Резервная копия сохранена: {backup_path}")
else:
    print("Файл не найден.")
