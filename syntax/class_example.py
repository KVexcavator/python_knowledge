class WizCoin:
  def __init__(self, galleons, sickles, knuts):
    self.galleons = galleons
    self.sickles = sickles
    self.knuts = knuts

  def value(self):
    return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts * 0.5)
  
  def wightInGrams(self):
    (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)

coinJar = WizCoin(13, 0, 0)
print(coinJar)
print("C:", coinJar.galleons)

# в Python нет фвногоопределения приватных или публичных методов
# в Python принято начинать имена приватных атрибутов и методов с одного символа подчеркивания. 
#  self._balance = 0
# Технически ничто не мешает коду за пределами класса обращаться к приватным атрибутам и методам,