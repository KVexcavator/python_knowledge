# технически каждый класс python исползует наследование
# все классы наследуются от класса object
# для примера это можно написать явно, это будет работать
from typing import List


class MySubClass(object):
  pass

class Contact:
  # переменная класса, расшарена между всеми инстансами класса и наследникаи
  all_contacts: List["Contact"] = []

  def __init__(self, name: str, email: str) -> None:
    self.name = name
    self.email = email
    Contact.all_contacts.append(self)

  def __repr__(self) -> str:
    return(
      f"{self.__class__.__name__}("
      f"{self.name!r}, {self.email!r}"
      f")"
    )
  
# >>> c_1 = Contact("Dog", "dog@example.local")
# >>> c_2 = Contact("Cat", "cat@xample.local")
# >>> Contact.all_contacts
# [Contact("Dog", "dog@example.local"), Contact("Cat", "cat@xample.local")]

class Order:
  pass

# Поставщик наследуется
class Supplier(Contact):
  def order(self, order: "Order") -> None:
    print(
      "If this were a real system we would send "
      f"'{order}' order to 'self.name'"
    )

# >>> c = Contact("Mouse", "mouse@example.local")
# >>> s = Supplier("Bear", "bear@example.local")
# >>> print(c.name, c.email, s.name, s.email)
# Mouse mouse@example.local Bear bear@example.local
# >>> from pprint import pprint
# >>> pprint(c.all_contacts)
# [Contact("Dog", "dog@example.local"),
# Contact("Cat", "cat@xample.local"),
# Contact("Mouse", "mouse@example.local"),
# Supplier("Bear", "bear@example.local")]
# >>> c.order("I need pliers")
# ....  AttributeError: 'Contact' object has no attribute 'order'
# >>> s.order("I need pliers")
# If this were a real system we would send 'I need pliers' order to 'Sup
# Plier'