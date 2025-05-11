# Локальный бэкап-менеджер с версионированием и логами
# Резервное копирование проектов, конфигураций, скриптов
import os
import shutil
from datetime import datetime
from rich import print

SOURCE_DIR = "my_project"
BACKUP_DIR = "backups"
MAX_VERSIONS = 5

os.makedirs(BACKUP_DIR, exist_ok=True)

def create_backup():
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  backup_path = os.path.join(BACKUP_DIR, f"{SOURCE_DIR}_{timestamp}")
  shutil.copytree(SOURCE_DIR, backup_path)
  print(f"[green] Бэкап создан:[/green] {backup_path}")
  manage_versions()

def manage_versions():
  versions = sorted(os.listdir(BACKUP_DIR))
  if len(versions) > MAX_VERSIONS:
    to_delete = versions[:-MAX_VERSIONS]
    for old in to_delete:
      shutil.rmtree(os.path.join(BACKUP_DIR, old))
      print(f"[yellow]🗑️ Удалена старая копия:[/yellow] {old}")

create_backup()

