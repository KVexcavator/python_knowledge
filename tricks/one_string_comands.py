# Сменка двух переменных
a = 4; b = 5
a,b = b,a
# Множественные присвоения переменных
a,b,c,d = 4,5.5,'Hello'
# или
a,b,*c = [1,2,3,4,5]
print(a,b,c) # > 1 2 [3,4,5]
# проверить являетсф число четным
is_even = lambda x: x % 2 == 0
# Сумма четных чисел в списке
a = [1,2,3,4,5,6]
s = sum([num for num in a if num%2 == 0])
print(s) # >> 12
# Удаление нескольких элементов из списка
a = [1,2,3,4,5]
del a[1::2]
print(a) # >[1, 3, 5]
# Чтение файлов
with open("data.txt") as f: lst=[line.strip() for line in f]
print(lst)
# Запись данных в файл
with open("data.txt",'a',newline='\n') as f: f.write("Python is awesome")
# прочитать файл в виде списка строк
line = open("file.txt").read().splitlines()
# Создание списков
lst = [i for i in range(0,10)]
# или
lst = list(range(0,10))
# или
lst = [("Hello "+i) for i in ['Karl','Abhay','Zen']]
print(lst) # > ['Hello Karl', 'Hello Abhay', 'Hello Zen']
# Mapping списков, или изменение типа данных в списке
list(map(int,['1','2','3']))
# > [1, 2, 3]
list(map(float,[1,2,3]))
# > [1.0, 2.0, 3.0]
# найти пересечение двух списков
intersection = list(set(list1) & set(list2))
# Создание набора
# Квадрат всех четных чисел в диапазоне
{x**2 for x in range(10) if x%2==0}
# > {0, 4, 16, 36, 64}
# Fizz Buzz
['FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i  for i in range(1,20)]
# Палиндром
text = 'level'
ispalindrome = text == text[::-1]
# Целые числа, разделенные пробелами, в списке
lis = list(map(int, input().split()))
print(lis) # > 1 2 3 4 5 6 7 8
#Функция, возвращающая квадрат любого числа
sqr = lambda x: x * x
# Проверить наличие числа в списке
num = 5
if num in [1,2,3,4,5]:
  print('present')
# найти самый часто встречающийся эломент в списке
most_common = max(set(list1), key=list1.count)
# Вывод паттернов
n = 5
print('\n'.join('?' * i for i in range(1, n + 1)))
# сплючить список саисков
flatList = [el for sulist in nestedList for el in sublist]
# создать словарь из двух списков
dictionary = dict(zip(sip(keys, values)))
# вычислить факториал
factorial = lambda n: 1 if n == 0 else n*factorial(n-1)
# сгенерировать Фибоначи
fibonacci = lambda n, a=0, b=1: a if n == 0 else fibonacci(n-1, b, a+b)
# трансформировать матрицу
transpose = list(zip(*matrix))
# обьеденить два словоря
merged_dict = {**dict1, **dict2}
# однострочный HTTP сервер
# python3 -m http.server
# отсортировать список кортежей по второму элоементу
sorted_tuples = sorted(tuples, key=lambda x: x[1])
# удалить дубликаты из спииска и сохранить порядок
unique_list = list(dict.fromkeys(lst))
# сумма квадратов чисел
sum_of_squares = sum(x**3 for x in range(10))
# проверить все ли элементы в списке уникальны
all_unique = len(lst) = len(set(lst))
# найти самое длинное слово
longest_word = max(sentence.split(), key=len)
# Простое число
list(filter(lambda x:all(x % y != 0 for y in range(2, x)), range(2, 13)))
# увеличить числа в списке в 2  разa
def scale(lst, x): return [i*x for i in lst] 
scale([2,3,4], 2)
# Замена текста другим текстом
"python is a programming language. python is python".replace("python",'Java')
# Симуляция подбрасывания монеты
import random; random.choice(['Head',"Tail"])
# Генерация групп
groups = [(a, b) for a in ['a', 'b'] for b in [1, 2, 3]] 
groups # > [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3)]