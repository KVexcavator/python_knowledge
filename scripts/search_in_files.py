# Локальный поисковик по файлам (txt, md, py, html и др.) с поддержкой фраз, ранжирования и подсветки
# Поиск по документации, заметкам, .md/.txt/.py файлам
# Локальный альтернативный поиск по коду
# Быстрая навигация в больших проектах
# Создание консольной справочной системы

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from rich.console import Console
from rich.markdown import Markdown

import os

# Создание схемы
schema = Schema(title=ID(stored=True), content=TEXT)

# Создание индекса
if not os.path.exists("index"):
  os.mkdir("index")
ix = create_in("index", schema)

# Индексация файлов
writer = ix.writer()
for root, _, files in os.walk("docs"):
  for file in files:
    if file.endswith((".txt", ".md", ".py", ".html")):
      path = os.path.join(root, file)
      with open(path, encoding="utf-8", errors="ignore") as f:
        content = f.read()
        writer.add_document(title=file, content=content)
writer.commit()
print("Индексация завершена.")

# Поиск
console = Console()
with ix.searcher() as searcher:
  query_str = input("Поиск: ")
  parser = QueryParser("content", schema=ix.schema)
  query = parser.parse(query_str)
  results = searcher.search(query, limit=5)

  if results:
    for hit in results:
      console.rule(f"[green]Файл: {hit['title']}")
      snippet = hit.highlights("content", top=3)
      console.print(Markdown(snippet))
  else:
    print("Ничего не найдено.")
