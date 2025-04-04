# pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
import json

URL = "https://profit.kz/companies/almaty/soft/softdevelopment/"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def extract_emails(url):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()  # если ошибка — выбросит исключение
    soup = BeautifulSoup(response.text, "html.parser")

    emails = []
    for a_tag in soup.select("a[href^=mailto]"):
        email = a_tag.get("href").replace("mailto:", "").strip()
        if email and email not in emails:
            emails.append(email)

    return emails

if __name__ == "__main__":
    emails = extract_emails(URL)

    with open("emails1.json", "w", encoding="utf-8") as f:
        json.dump(emails, f, ensure_ascii=False, indent=2)

    print(f"Извлечено {len(emails)} email(ов). Сохранено в emails.json")
