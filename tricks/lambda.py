# базовая lambda-функция
add = lambda x, y: x + y
# lambda с map
nums = [1,2,3,4,5]
squares = list(map(lambda x: x**2, nums))
# lambda c filter
nums = [1,2,3,4,5]
events = list(filter(lambda x: x % 2 == 0, nums))
# lambda c reduce
from functools import reduce
nums = [1,2,3,4,5]
product = reduce(lambda x, y: x*y, nums)
# сортировка с lambda
pairs = [(1,2),(3,1),(5,4),(2,3)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
# условная lambda
max_num = lambda x, y: x if x > y else y
print(max_num(10, 20))
# однострочное списковое включение
nums = [1,2,3,4,5,6]
squares = [x**2 for x in nums if x % 2 == 0]
print(squares) # [4, 16, 36]
# oднострочное словарное включени
nums = [1,2,3]
squares = {x: x**2 for x in nums}
print(squares)# {1: 1, 2: 4, 3: 9}
# тернальный оператор в одну строчку
age = 18
status = 'Adult' if age >= 18 else "Minor"
# lambda внутри функции
def sort_by_key(data, key):
  return sorted(data, key=lambda x: k[key])
students = [
  {'name': 'Bob', 'score': 85},
  ...
]
sorted_students = sort_by_key(students, 'score')