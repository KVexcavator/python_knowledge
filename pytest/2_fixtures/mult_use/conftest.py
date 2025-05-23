import cards
import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest

@pytest.fixture(scope="session")
def cards_db():
  with TemporaryDirectory() as db_dir:
    db_path = Path(db_dir)
    db = cards.CardsDB(db_path)
    yield db
    db.close()

@pytest.fixture(scope="session")
def some_cards():
  """List of different Card objects"""
  return[
    cards.Card("write book", "Brian", "done"),
    cards.Card("edit book", "Katie", "done"),
    cards.Card("write 2nd edition", "Brian", "todo"),
    cards.Card("edit 2nd edition", "Katie", "todo"),
  ]

@pytest.fixture(scope="function")
def non_empty_db(cards_db, some_cards):
  """CardsDB object that's been populated with 'some_cards'"""
  for c in some_cards:
    cards_db.add_card(c)
  return cards_db