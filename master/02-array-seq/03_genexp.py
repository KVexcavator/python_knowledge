# genexp генераторное выражение 
# экономит память, т. к. отдает элементы по одному
# заключается не в квадратные скобки, а в круглые

symbols = '$¢£¥€¤'
tuple(ord(symbol) for symbol in symbols) # (36, 162, 163, 165, 8364, 164)

import array
array.array('I', (ord(symbol) for symbol in symbols)) # array('I', [36, 162, 163, 165, 8364, 164])

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in (f'{c} {s}' for c in colors for s in sizes):
  print(tshirt)
# отдает по одному элементу за раз; список, содержащий все шесть вариаций футболки, не создается
# black S
# black M ...