# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

var_1 = 'Переменная 1'
var_2 = 'Переменная 2'

print(var_1)
print(var_2)

num_1, num_2 = map(int, input('Введите два числа через пробел: ').split())
str_1, str_2 = input('Введите два слова через пробел: ').split()

print(f'num_1 = {num_1}, num_2 = {num_2}')
print(f'str_1 = {str_1}, str_2 = {str_2}')
