# Извлечение данных из PDF-таблицы
#
import pdfplumber
import pandas as pd
import os

PDF_PATH = "sample_invoice.pdf"

def extract_tables(pdf_path):
  dataframes = []
  with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
      tables = page.extract_tables()
      for table in tables:
        df = pd.DataFrame(table[1:], columns=table[0])
        dataframes.append(df)
  return dataframes

tables = extract_tables(PDF_PATH)

# Сохраняем первую таблицу
if tables:
  output_file = "invoice_data.csv"
  tables[0].to_csv(output_file, index=False)
  print(f"Данные извлечены и сохранены в {output_file}")
else:
  print("Таблиц не найдено в PDF")
