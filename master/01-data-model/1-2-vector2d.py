# операции с двухмерными векторами
import math

class Vector:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __repr__(self):
    return f'Vector({self.x!r}, {self.y!r})'
  # возвращает абсолютную величину вещественного числа
  def __abs__(self):
    return math.hypot(self.x, self.y)
  
  def __bool__(self):
    return bool(abs(self))
  
  def __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x, y)  
  # * умножение вектора на число, в результате которого получается новый вектор с тем же направлением и умноженным на данное число модулем
  def __mul__(self, scalar):
    return Vector(self.x * scalar, self.y * scalar)
  
v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2) # Vector(4, 5)
v = Vector(3, 4)
print(abs(v)) # 5.0
print(v * 3) # Vector(9, 12)
print(abs(v * 3)) # 15.0
