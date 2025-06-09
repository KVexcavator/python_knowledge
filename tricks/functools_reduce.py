# последовательно применять функцию к элементам итерируемого объекта, сворачивая его к одному результату
from functools import reduce  

numbers = [1, 2, 3, 4]  
product = reduce(lambda x, y: x * y, numbers)  
print(product)  # 24
