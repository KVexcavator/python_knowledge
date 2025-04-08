from docx import Document

# Загрузка шаблона
doc = Document("template.docx")

# Данные для подстановки
data = {
    "{{number}}": "2024/015",
    "{{city}}": "Москва",
    "{{date}}": "28.03.2025",
    "{{client}}": "Иванов И.И.",
    "{{amount}}": "150000"
}

# Замена текста в каждом абзаце
for paragraph in doc.paragraphs:
    for key, value in data.items():
        if key in paragraph.text:
            paragraph.text = paragraph.text.replace(key, value)

# Сохраняем результат
output_filename = "filled_contract.docx"
doc.save(output_filename)
print(f"Документ создан: {output_filename}")
