# Given/Arrange - дано, начальное состояние. Здесь вы настраиваете данные или среду для подготовки к действию.
# When/Act - выполняется какое-то действие. Это фокус теста — поведение, которое мы пытаемся проверить, работает ли оно правильно.
# Then/Assert - должен произойти какой-то ожидаемый результат или конечное состояние. В конце теста мы убеждаемся, что действие привело к ожидаемому поведению.

from cards import Card

def test_to_dict():
  # GIVEN a Card object with known contents
  c1 = Card("something", "brian", "todo", 123)
  # WHEN we call to_dict() on the object
  c2 = c1.to_dict()
  # THEN the result will be a dictionary with known content
  c2_expected = {
    "summary": "something",
    "owner": "brian",
    "state": "todo",
    "id": 123,
  }
  assert c2 == c2_expected