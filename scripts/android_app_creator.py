# Создание APK из HTML+CSS+JSG (веб-приложения)
# Требования: -Node.js и Cordova
# npm install -g cordova
import os
import subprocess
import shutil

PROJECT_NAME = "webapk"
INDEX_HTML_PATH = "my_web/index.html"  # твой HTML
OUTPUT_DIR = os.path.abspath("output_apk")

def run(cmd):
  print(f" {cmd}")
  subprocess.run(cmd, shell=True, check=True)

def main():
  if os.path.exists(PROJECT_NAME):
    shutil.rmtree(PROJECT_NAME)

  print("Создаём Cordova-проект...")
  run(f"cordova create {PROJECT_NAME} com.example.webapk WebApp")
  os.chdir(PROJECT_NAME)

  print("Добавляем Android-платформу...")
  run("cordova platform add android")

  print("Копируем HTML-файлы...")
  shutil.copyfile(os.path.abspath(INDEX_HTML_PATH), "www/index.html")

  print("Собираем APK...")
  run("cordova build android")

  apk_path = os.path.join("platforms", "android", "app", "build", "outputs", "apk", "debug", "app-debug.apk")
  os.makedirs(OUTPUT_DIR, exist_ok=True)
  shutil.copy(apk_path, os.path.join(OUTPUT_DIR, "webapp.apk"))

  print(f"\nГотово! APK: {os.path.join(OUTPUT_DIR, 'webapp.apk')}")

if name == "main":
    main()
