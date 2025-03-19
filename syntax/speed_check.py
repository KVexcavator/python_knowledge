# Использование модуля timeit для оценки быстродействия
import timeit
timeit.timeit('a, b = 42, 101; a = a ^ b; b = a ^ b; a = a ^ b')