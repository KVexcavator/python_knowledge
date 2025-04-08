# Переопределение означает изменение или замену метода суперкласса новым методом (с тем же именем) в подклассе.
from .basic import Contact

class Friend(Contact):
  def __init__(self, name: str, email: str, phone: str) -> None:
    super().__init__(name, email)
    self.phone = phone