# планировщик задач
import schedule
import time
from datetime import datetime

# Пример задач
def backup():
    print(f"💾 [BACKUP] Резервная копия в {datetime.now().strftime('%H:%M:%S')}")

def clean_temp():
    print(f"🧹 [CLEAN] Очистка временных файлов в {datetime.now().strftime('%H:%M:%S')}")

def report():
    print(f"📊 [REPORT] Генерация отчета в {datetime.now().strftime('%H:%M:%S')}")

# Расписание задач
schedule.every().day.at("09:00").do(backup)
schedule.every(10).minutes.do(clean_temp)
schedule.every().monday.at("08:00").do(report)

print("🕒 Планировщик запущен. Нажми Ctrl+C для выхода.")

# Основной цикл
while True:
    schedule.run_pending()
    time.sleep(1)
