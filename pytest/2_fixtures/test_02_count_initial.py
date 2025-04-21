# Первоначальный тест, проверяющий, что отсчет начинается с нуля, может выглядеть следующим образом, но работать не будет:
from pathlib import Path
from tempfile import TemporaryDirectory
import cards

def test_empty():
  with TemporaryDirectory() as db_dir:
    db_path = Path(db_dir)
    db = cards.CardsDB(db_path)

    count = db.count
    # закрывается не выполнив тест
    db.close()

    assert count == 0

# pytest test_02_count_initial.py