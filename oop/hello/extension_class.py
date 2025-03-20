# класс можно писать где угодно, здесь пример классв абстакуции, и его расширения внутри метода
from typing import Optional

class Formatter:
  def format(self, string: str) -> str:
    pass

def format_string(string: str, formatter: Optional[Formatter] = None)-> str:

  class DefaultFormatter(Formatter):
    def format(self, string: str) -> str:
      return str(string).title()
    
  if not formatter:
    formatter = DefaultFormatter()

  return formatter.format(string)

# >>> hello_string = "hello world, how are you today?"
# >>> print(f" input: {hello_string}")
# input: hello world, how are you today?
# >>> print(f"output: {format_string(hello_string)}")
# output: Hello World, How Are You Today?