# Моделирование игр, в которых задействованы многогранные кости.
# В Python существует три легкодоступных источника случайных данных: модуль random, модуль os и модуль secrets.
import abc
import random

class Die(abc.ABC):
  def __init__(self) -> None:
    self.face: int
    self.roll()

  @abc.abstractmethod
  def roll(self) -> None:
    ...

  def __repr__(self) -> str:
    return f"{self.face}"
  
# Четырехгранная игральная кость использует random.choice().
class D4(Die):
  def roll(self) -> None:
    self.face = random.choice((1, 2, 3, 4)) 
# Шестигранная игральная кость — обычный куб, известный большинству людей — использует random.randint().
class D6(Die):
  def roll(self) -> None:
    self.face = random.randint(1, 6)