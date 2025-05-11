# Индексация PDF-файлов и интеллектуальный поиск по ним (PDF → база знаний)
# например: поиск по нормативке, договорам, архивам
import os
from PyPDF2 import PdfReader
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from rich.console import Console
from rich.markdown import Markdown

# Шаг 1: создание индекса
schema = Schema(title=ID(stored=True), content=TEXT)
os.makedirs("index", exist_ok=True)
ix = create_in("index", schema)
writer = ix.writer()

# Шаг 2: загрузка PDF и индексация
for file in os.listdir("pdfs"):
  if file.endswith(".pdf"):
    path = os.path.join("pdfs", file)
    reader = PdfReader(path)
    full_text = "\n".join(page.extract_text() or "" for page in reader.pages)
    writer.add_document(title=file, content=full_text)

writer.commit()
print("Все PDF проиндексированы.")

# Шаг 3: Поиск
console = Console()
with ix.searcher() as searcher:
  query_str = input("Поиск: ")
  parser = QueryParser("content", schema=ix.schema)
  query = parser.parse(query_str)
  results = searcher.search(query, limit=5)

  if results:
    for hit in results:
      console.rule(f"[green]Документ: {hit['title']}")
      snippet = hit.highlights("content", top=3)
      console.print(Markdown(snippet))
  else:
    print("Ничего не найдено.")
