# Этот класс расширяет встроенный список. Мы предоставили подсказку типа, предполагающую, что мы создаем список только целочисленных объектов. Для этого мы переопределили метод append для проверки двух условий, которые гарантируют, что элемент является четным целым числом.
from typing import List

class EventOnly(List[int]):
  def append(self, value: int) -> None:
    if not isinstance(value, int):
      raise TypeError("Only integer can be added")
    if value % 2 !=0:
      raise ValueError("Only even numbers can be added")
    super().append(value)

# этот клас только демонстрирует, в боевом применении, требуется переопределить также extend(), insert(), __setitem__() и даже __init__()