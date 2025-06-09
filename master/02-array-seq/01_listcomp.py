# listcomp списковое включение
# genexp генераторное выражение

# без генератора
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
  codes.append(ord(symbol))

print(codes) # [36, 162, 163, 165, 8364, 164]

# c генераором и списковым включением
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes) # [36, 162, 163, 165, 8364, 164]

# списковое включение может делать все, что умеют функции map и filter
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii) # [162, 163, 165, 8364, 164]

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii) # [162, 163, 165, 8364, 164]