# print "hello world"
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hello world")?

x = 5 / 0
# ZeroDivisionError: division by zero

lst = [1,2,3]
print(lst[3])
# IndexError: list index out of range

lst + 2
# TypeError: can only concatenate list (not "int") to list

lst.add
# AttributeError: 'list' object has no attribute 'add'

d = {'a': 'hello'}
d['b']
# KeyError: 'b'

print(this_is_not_a_var)
# NameError: name 'this_is_not_a_var' is not defined