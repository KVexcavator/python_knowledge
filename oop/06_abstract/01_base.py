# Создание абстрактного базового класса
# https://docs.python.org/3/library/abc.html
# Пример, создаем медиаплеер с сторонними плагинами. 
import abc

class MediaLoader(abc.ABC):
  @abc.abstractmethod
  def play(self) -> None:
    ...
  @property
  @abc.abstractmethod
  def ext(self) -> str:
    ...
# вывести список абстрактных методов
MediaLoader.__abstractmethods__
# abc.ABC метакласс — класс, используемый для построения конкретных определений классов,по умолчанию называется type. 
# class Wav(MediaLoader):
#   pass
# x = Wav() вернет ошибку
# class Ogg(MediaLoader):
#   ext = '.ogg'
#   def play(self):
#     pass
# o = Ogg() пройдет без ошибок