# Колода как последовательность карт
import collections
# здесь используется класс namedtuple для построения класса, который содержит только атрибуты и никаких методов
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
  ranks = [str(n) for n in range(2,11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks] 

  def __len__(self):
    return len(self._cards)
  
  def __getitem__(self, position):
    return self._cards[position]
  
    
beer_card = Card('7', 'diamonds')
print(beer_card)
deck = FrenchDeck()
# __len__ получаем длину
print(len(deck))
# __getitem__ дает доступ к []
print(deck[0])
print(deck[-1])
# вызвать случайную
from random import choice
print(choice(deck))
# __getitem__ поддерживает срезы
print(deck[:3])
# __getitem даёт итерирование в любом направлении
for card in reversed(deck):
  print(card)

print('=======sort========')
# Сортировка: обычно карты ранжируются по достоинству (тузы – самые старшие), а затем по масти в порядке пики (старшая масть), черви, бубны и трефы (младшая масть)
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
  rank_value = FrenchDeck.ranks.index(card.rank)
  return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
  print(card)

# Вследствие реализации специальных методов __len__ и __getitem__ класс FrenchDeck ведет себя как стандартная последовательность и позволяет использовать базовые средства языка (например, итерирование и получение среза),а также функции reversed и sorted. Благодаря композиции реализации методов __len__ и __getitem__ могут перепоручать работу объекту self._cards класса list.