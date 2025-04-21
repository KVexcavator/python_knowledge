# Клонирование голоса и синтез речи
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice

tts = TextToSpeech()

# Загрузка примера голоса (нужен 1–2 аудиофайла)
voice_samples = load_voice("my_voice")  # папка с .wav файлами

# Текст, который нужно озвучить
text = "Привет! Это я говорю сам с собой, но в другом времени."

# Генерация аудио
gen = tts.tts_with_preset(text, voice_samples, preset="fast")  # или "high_quality"

# Сохраняем результат
gen.save("my_clone_output.wav")
print("Синтез завершён: my_clone_output.wav")
