# Генерация видео из изображений и текста

from moviepy.editor import *

# Создаём титр/слайд
def create_slide(text, duration=3):
    clip = TextClip(text, fontsize=60, color='white', bg_color='black', size=(1280, 720))
    return clip.set_duration(duration)

# Список слайдов
slides = [
    create_slide("Привет! Это видео сгенерировано на Python."),
    create_slide("Каждый слайд — это просто текст."),
    create_slide("Можно добавлять изображения, звук и даже анимации!")
]

# Объединение и экспорт
final = concatenate_videoclips(slides, method="compose")
final.write_videofile("output_video.mp4", fps=24)
