# можем поймать проблему, если не будем чисть базу в conftest.py
# pytest -v --tb=line mult_levels/test_count.py mult_levels/test_three.py
import cards

def test_two(cards_db):
  cards_db.add_card(cards.Card("first"))
  cards_db.add_card(cards.Card("second"))
  cards_db.add_card(cards.Card("third"))
  assert cards_db.count() == 3

  # pytest --setup-show mult_levels/test_three.py