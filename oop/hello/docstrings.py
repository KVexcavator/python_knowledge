# документирование класса
# python3 -m doctest docstrings.py
# python3 -i docstrings.py
# >>> help(Point)
import math
class Point:
  """
  Represents a point in two-dimensional geometric coordinates
  >>> p_0 = Point()
  >>> p_1 = Point(3, 4)
  >>> p_0.calculate_distance(p_1)
  5.0
  """
  def __init__(self, x: float = 0, y: float = 0) -> None:
    """
    Initialize the position of a new point. The x and ycoordinates can be specified. If they are not, the
    point defaults to the origin.
    :param x: float x-coordinate
    :param y: float x-coordinate
    """
    self.move(x, y)

  def move(self, x: float, y: float) -> None:
    """
    Move the point to a new location in 2D space.
    :param x: float x-coordinate
    :param y: float x-coordinate
    """
    self.x = x
    self.y = y
  def reset(self) -> None:
    """
    Reset the point back to the geometric origin: 0, 0
    """
    self.move(0, 0)

  def calculate_distance(self, other: "Point") -> float:
    """
    Calculate the Euclidean distance from this point
    to a second point passed as a parameter.
    :param other: Point instance
    :return: float distance
    """
    return math.hypot(self.x - other.x, self.y - other.y)