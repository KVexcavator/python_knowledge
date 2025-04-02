from cards import Card

def test_equality_fall():
  c1 = Card("sit there", "brian")
  c2 = Card("do something", "okken")
  assert c1 == c2

# pytest -vv test_equality_fall.py