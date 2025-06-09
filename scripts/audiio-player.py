# плеер аудиокниг/подкастов с закладками и продолжением с места
import pygame
import time
import os
import json

AUDIO_FILE = "audiobook.mp3"
PROGRESS_FILE = "progress.json"

pygame.mixer.init()
pygame.mixer.music.load(AUDIO_FILE)

if os.path.exists(PROGRESS_FILE):
  with open(PROGRESS_FILE) as f:
    data = json.load(f)
    position = data.get(AUDIO_FILE, 0)
    print(f"Продолжаем с {round(position, 2)} сек")
else:
  position = 0

pygame.mixer.music.play(start=position)

try:
  while pygame.mixer.music.get_busy():
    time.sleep(1)
except KeyboardInterrupt:
  current_pos = pygame.mixer.music.get_pos() / 1000 + position
  with open(PROGRESS_FILE, "w") as f:
    json.dump({AUDIO_FILE: current_pos}, f)
  print(f"\nОстановлено на {round(current_pos, 2)} сек. Позиция сохранена.")
