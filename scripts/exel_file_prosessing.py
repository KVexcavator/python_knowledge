# Автоматическая обработка Excel-файла с фильтрацией, расчётами и экспортом
import pandas as pd

# Загружаем Excel-файл
df = pd.read_excel("sales.xlsx")

# Фильтрация по дате и сумме
df_filtered = df[(df["Сумма"] > 10000) & (df["Дата"] >= "2024-01-01")]

# Добавляем колонку "С НДС"
df_filtered["Сумма с НДС"] = df_filtered["Сумма"] * 1.2

# Группировка по менеджеру
grouped = df_filtered.groupby("Менеджер")["Сумма с НДС"].sum().reset_index()
grouped = grouped.sort_values(by="Сумма с НДС", ascending=False)

# Сохраняем результаты
df_filtered.to_excel("filtered_sales.xlsx", index=False)
grouped.to_excel("summary_by_manager.xlsx", index=False)

print("Отчёты созданы: filtered_sales.xlsx и summary_by_manager.xlsx")

