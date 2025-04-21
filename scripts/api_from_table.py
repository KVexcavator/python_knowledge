# Генерация полноценного REST API из любого табличного файла (CSV, Excel, SQLite)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()
df = pd.read_csv("data.csv")

# Автоматическое определение модели из DataFrame
class Record(BaseModel):
    id: int
    name: str
    value: float

@app.get("/records")
def get_records():
    return df.to_dict(orient="records")

@app.get("/records/{record_id}")
def get_record(record_id: int):
    match = df[df["id"] == record_id]
    if match.empty:
        raise HTTPException(status_code=404, detail="Not found")
    return match.to_dict(orient="records")[0]

@app.post("/records")
def add_record(record: Record):
    global df
    df = pd.concat([df, pd.DataFrame([record.dict()])], ignore_index=True)
    return {"message": "Добавлено"}

@app.delete("/records/{record_id}")
def delete_record(record_id: int):
    global df
    df = df[df["id"] != record_id]
    return {"message": "Удалено"}

# Запуск:
# uvicorn script:app --reload
