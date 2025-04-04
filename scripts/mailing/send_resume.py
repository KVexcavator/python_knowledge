# pip install secure-smtplib
# pip install python-dotenv

import smtplib
import ssl
import json
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()
sender_email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

subject = "Fullstack developer resume"
body = """\
Здравствуйте
Я Software Fullstack engineer (Ruby, Python, React)
Я занимаюсь разработкой на Ruby с 2015 года. Мой опыт охватывает различные области, от розничной торговли продуктами до финтеха, с использованием Ruby on Rails версий 4–7. Кроме того, я разрабатываю фронтенды с помощью React.
Сейчас я живу в Aлматы (гр. Казахстана) и ищу работу в дружественной компании.
По любым вопросам:
мой телеграм: @kvexcavator, часовой пояс: +6 GMT

С наилучшими пожеланиями,  
Вячеслав Каландаришвили
(Это письмо автоматически было сгенерированно моим скриптом)
"""

# Загрузка email-адресов из JSON
with open("emails_trade1.json", "r", encoding="utf-8") as f:
    recipients = json.load(f)

# Загрузка резюме один раз
with open("Software_Fullstack_Engineer_ru.pdf", "rb") as f:
    resume_data = f.read()
    resume_filename = "Vyacheslav_developer_resume.pdf"

# Установка защищённого соединения
context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls(context=context)
    server.login(sender_email, password)

    for recipient in recipients:
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender_email
        msg["To"] = recipient
        msg.set_content(body)
        msg.add_attachment(resume_data, maintype="application", subtype="pdf", filename=resume_filename)

        try:
            server.send_message(msg)
            print(f"Отправлено: {recipient}")
        except Exception as e:
            print(f"Ошибка при отправке на {recipient}: {e}")
