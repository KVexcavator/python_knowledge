# Думайте о функции свойства(property function) как о возвращающем объекте, который проксирует любые запросы на получение или установку значения атрибута через указанные нами имена методов.

class NorwegianBlue:
  def __init__(self, name: str) -> None:
    self._name = name
    self._state: str

  def _get_state(self) -> str:
    print(f"Getting {self._name}'s State: {self._state!r}")
    return self._state
  
  def _set_state(self, state: str) -> None:
    print(f"Setting {self._name}'s State to {state!r}")
    self._state = state

  def _del_state(self) -> None:
    print(f"{self._name} is pushing up daisies!")
    del self._state

  silly = property(
    _get_state, _set_state, _del_state,
    "This is a silly property"
  )

# при вызове методов появляется сотояние
p = NorwegianBlue("Polly")
p.silly = "Logging and do some..."
# Setting Polly's State to 'Logging and do some...'
p.silly
# Getting Polly's State: 'Logging and do some...'
del p.silly
# Polly is pushing up daisies!