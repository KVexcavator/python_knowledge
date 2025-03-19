# часто пишут
animals = ['cat', 'dog', 'moose']
for i in range(len(animals)):
  print(i, animals[i])
# всесто этого
for i, animal in enumerate(animals):
  print(i, animal)
# если индексы не нужны
for animal in animals:
  print(animal)