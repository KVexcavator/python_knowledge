# Управление Android-устройством с компьютера через ADB
from ppadb.client import Client as AdbClient

client = AdbClient(host="127.0.0.1", port=5037)
device = client.devices()[0]

print(f"Подключено к: {device.serial}")

# Сделать скриншот
screencap = device.screencap()
with open("screenshot.png", "wb") as f:
  f.write(screencap)
print("Скриншот сохранён.")

# Ввод текста
device.shell('input text "Hello_from_Python"')

# Нажатие кнопки "Назад"
device.shell("input keyevent 4")

# Запуск приложения
device.shell("am start -n com.android.chrome/com.google.android.apps.chrome.Main")
