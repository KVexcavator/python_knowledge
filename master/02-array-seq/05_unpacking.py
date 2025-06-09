#
#
#

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates 

# обмен значениями
b, a = 10, 20
b, a = a, b

# прменение звездочки перед аргументом
t = (20, 8)
divmod(*t) # (2, 4)
quotient, remainder = divmod(*t)
quotient # 2
quotient, remainder # (2, 4)

# * для выборки лишних элементов
a, b, *rest = range(5)
a, *body, c, d = range(5)
*head, b, c, d = range(5)

# * в вызовах функций и литеральных последовательностях
def fun(a, b, c, d, *rest):
  return a, b, c, d, rest
# использовать несколко раз при вызове
fun(*[1, 2], 3, *range(4, 7)) # (1, 2, 3, 4, (5, 6))
# * можно также использовать при определении литералов типа list, tuple и set
*range(4), 4 # (0, 1, 2, 3, 4)
[*range(4), 4] # [0, 1, 2, 3, 4]
{*range(4), 4, *(5, 6, 7)} # {0, 1, 2, 3, 4, 5, 6, 7}