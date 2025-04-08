# определение кастомных исключений

# class InvalidSomething(ValueError):
#   pass

# raise InvalidSomething("You don't have $50 in your account")
# InvalidWithdrawal: You don't have $50 in your account

# withdrawal снятие
from decimal import Decimal

class InvalidWithDrawal(ValueError):
  def __init__(self, balance: Decimal, amount: Decimal) -> None:
    super().__init__(f"account doesn't have ${amount}")
    self.amount = amount
    self.balance = balance

  def overage(self) -> Decimal:
    return self.amount - self.balance

# напрямую
# raise InvalidWithdrawal(Decimal('25.00'), Decimal('50.00'))
# ...
# InvalidWithdrawal: account doesn't have $50.00

# пряморукая обрабатка исключения InvalidWithdrawal, если таковое возникнет:
try:
  balance = Decimal('25.00')
  raise InvalidWithDrawal(balance, Decimal('50.00'))
except InvalidWithDrawal as ex:
  print(
    "I'm sorry, but your withdrawal is "
    "more than your balance by "
    f"${ex.overage()}"
  )
# I'm sorry, but your withdrawal is more than your balance by $25.00