# свойсва можно создать с помощю декораторов

class NorwegianBlue:
  def __init__(self, name: str) -> None:
    self._name = name
    self._state: str

  @property
  def silly(self) -> str:
    """This is a silly property"""
    print(f"Getting {self._name}'s State: {self._state!r}")
    return self._state
  
  @silly.setter
  def silly(self, state: str) -> None:
    print(f"Setting {self._name}'s State to {state!r}")
    self._state = state

  @silly.deleter
  def silly(self) -> None:
    print(f"{self._name} is pushing up daisies!")
    del self._state

p = NorwegianBlue("Polly")
p.silly = "Logging and do some..."
# Setting Polly's State to 'Logging and do some...'
p.silly
# Getting Polly's State: 'Logging and do some...'
del p.silly
# Polly is pushing up daisies!