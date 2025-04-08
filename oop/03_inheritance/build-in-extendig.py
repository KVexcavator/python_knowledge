# Расширение встроенных функций
# добавление функциональности к встроенным классам с помощью наследования от встроенного типа

# __future__ — это специальный модуль, который позволяет включить функции будущих версий Python в текущей версии
from __future__ import annotations

class ContactList(list["Contact"]):

  def search(self, name: str) -> list["Contact"]:
    matching_contacts: list["Contact"] = []
    for contact in self:
      if name in contact.name:
        matching_contacts.append(contact)
    return matching_contacts
  
class Contact:
  all_contacts = ContactList()

  def __init__(self, name: str, email: str) -> None:
    self.name = name
    self.email = email
    Contact.all_contacts.append(self)

  def __repr__(self) -> str:
    return(
      f"{self.__class__.__name__}("
      f"{self.name!r}, {self.email!r}" f")"
    )
  
# >>> c1 = Contact("John A", "johna@example.net")
# >>> c2 = Contact("John B", "johnb@sloop.net")
# >>> c3 = Contact("Jenna C", "cutty@sark.io")
# >>> [c.name for c in Contact.all_contacts.search('John')]
# ['John A', 'John B']