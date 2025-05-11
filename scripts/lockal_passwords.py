# Локальный менеджер паролей
# Личный менеджер паролей
# Безопасное хранение токенов, ключей API, PIN-кодов
# Встроить в приложения, Telegram-ботов, DevOps-скрипты
# Лёгкая и офлайн-замена сторонним сервисам типа 1Password
from cryptography.fernet import Fernet
import json
import os

# Генерация или загрузка ключа шифрования
KEY_FILE = "secret.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

cipher = load_key()

# Файл для хранения паролей
DATA_FILE = "passwords.json"

def load_passwords():
  if not os.path.exists(DATA_FILE):
    return {}
  with open(DATA_FILE, "r") as f:
    encrypted_data = f.read()
    if not encrypted_data:
      return {}
    decrypted_data = cipher.decrypt(encrypted_data.encode()).decode()
    return json.loads(decrypted_data)

def save_passwords(passwords):
  encrypted_data = cipher.encrypt(json.dumps(passwords).encode())
  with open(DATA_FILE, "w") as f:
    f.write(encrypted_data.decode())

def add_password(service, password):
  passwords = load_passwords()
  passwords[service] = password
  save_passwords(passwords)
  print(f"Пароль для {service} сохранён.")

def get_password(service):
  passwords = load_passwords()
  if service in passwords:
    print(f"Пароль для {service}: {passwords[service]}")
  else:
    print("Сервис не найден.")

def delete_password(service):
  passwords = load_passwords()
  if service in passwords:
    del passwords[service]
    save_passwords(passwords)
    print(f"🗑️ Пароль для {service} удалён.")
  else:
    print("Сервис не найден.")

# --- Пример использования ---
# add_password("github", "mygithubpassword123")
# get_password("github")
# delete_password("github")
