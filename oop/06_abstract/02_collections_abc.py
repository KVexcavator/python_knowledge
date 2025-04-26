# Действительно всеобъемлющее использование абстрактных базовых классов в стандартной библиотеке Python находится в модуле collections. Коллекции, которые мы используем, являются расширениями абстрактного класса Collection. Collection — это расширение еще более фундаментальной абстракции, Container.
from collections.abc import Container
Container.__abstractmethods__
# frozenset({'__contains__'})
# Container имеет один метод который нужно реализовать
# Этот метод реализуется с помощью set, list, str, tuple и dict. Однако мы также можем определить , например, контейнер, который сообщает нам, находится ли заданное значение в наборе нечетных целых чисел:
class OddIntegers:
  def __contains__(self, x: int) -> bool:
    return x % 2 != 0

odd = OddIntegers()
isinstance(odd, Container)
# True
issubclass(OddIntegers, Container)
# True
1 in odd
# True
2 in odd
# False
3 in odd
# True

# The collections.abc module
# Этот модуль предоставляет определения абстрактного базового класса для встроенных коллекций Python, list, set и dict и несколько других могут быть построены из отдельных определений компонентов.
# Определения в collections.abc предоставляет определения MutableSequence, MutableMapping и MutableSet, которые являются абстрактными базовыми классами для list, dict или set.
