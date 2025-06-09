# Поисковый движок по PDF-архиву (быстро, офлайн, с индексом)
import os
import pdfplumber
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser

PDF_DIR = "pdfs"
INDEX_DIR = "indexdir"

# 1. Схема индекса
schema = Schema(title=ID(stored=True), content=TEXT)

# 2. Создание/очистка индекса
if not os.path.exists(INDEX_DIR):
  os.mkdir(INDEX_DIR)
  ix = index.create_in(INDEX_DIR, schema)
else:
  ix = index.open_dir(INDEX_DIR)

# 3. Индексация PDF-файлов
writer = ix.writer()
for filename in os.listdir(PDF_DIR):
  if filename.endswith(".pdf"):
    path = os.path.join(PDF_DIR, filename)
    try:
      with pdfplumber.open(path) as pdf:
        text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        writer.add_document(title=filename, content=text)
        print(f"Индексирован: {filename}")
    except Exception as e:
        print(f"Проблема с {filename}: {e}")
writer.commit()

# 4. Поиск
search_query = input("Поисковый запрос: ")
with ix.searcher() as searcher:
  parser = QueryParser("content", ix.schema)
  query = parser.parse(search_query)
  results = searcher.search(query, limit=10)
  if results:
    print("🔎 Найдено в файлах:")
    for r in results:
      print("—", r["title"])
  else:
    print("Ничего не найдено.")
