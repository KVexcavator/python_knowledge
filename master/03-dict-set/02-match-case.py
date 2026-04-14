# Сопоставление с отображением-образцом

def get_creators(record: dict) -> list:
  match record:
    case {'type': 'book', 'api': 2, 'authors': [*names]}:
      return names
    case {'type': 'book', 'api': 1, 'author': name}:
      return [name]
    case {'type': 'book'}:
      raise ValueError(f"Invalid 'book' record: {record!r}")
    case {'type': 'movie', 'director': name}:
      return [name]
    case _:
      raise ValueError(f'Invalid record: {record!r}')
    
b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Gödel, Escher, Bach')
print(get_creators(b1))