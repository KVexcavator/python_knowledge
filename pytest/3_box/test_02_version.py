# проверяем что вызов в баше card.version будет еквивалентен выводу в средеисполнения python

import cards
def test_version_v2(capsys):
  cards.cli.version()
  output = capsys.readouterr().out.rstrip()
  assert output == cards.__version__