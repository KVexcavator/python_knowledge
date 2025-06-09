# Трекер активности пользователя (движения мыши, клики, нажатия клавиш)
from pynput import keyboard, mouse
import time
from datetime import datetime

last_active = time.time()
IDLE_THRESHOLD = 60  # секунд бездействия
log = []

def update_activity():
  global last_active
  last_active = time.time()

def on_press(key):
  update_activity()

def on_click(x, y, button, pressed):
  update_activity()

# Запуск слушателей
keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener.start()
mouse_listener.start()

print("Монитор активности запущен. Нажмите Ctrl+C для остановки.")
try:
  while True:
    now = time.time()
    idle_time = now - last_active
    if idle_time < IDLE_THRESHOLD:
      log.append((datetime.now(), "Активен"))
    else:
      log.append((datetime.now(), "Бездействие"))
    time.sleep(60)
except KeyboardInterrupt:
  print("\nЛог активности:")
  for entry in log:
    print(f"{entry[0].strftime('%H:%M:%S')} — {entry[1]}")
