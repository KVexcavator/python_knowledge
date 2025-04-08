# Самая простая и полезная форма множественного наследования следует шаблону проектирования, называемому миксин.
from .basic import Contact
from typing import Protocol

# Protocol позволяет объявить контракт, похож на интерфейсы
class Emailable(Protocol):
  email: str

# здесь подмешивается атрибут email
class MailSender(Emailable):
  def send_mail(self, message: str) -> None:
    print(f"Sending mail to {self.email=}")

# здесь подмешиваем два класса
class EmailableContact(Contact, MailSender):
  pass

# >>> e = EmailableContact("John B", "johnb@sloop.net")
# >>> Contact.all_contacts
# [EmailableContact('John B', 'johnb@sloop.net')]
# >>> e.send_mail("Hello, test e-mail here")
# Sending mail to self.email='johnb@sloop.net'