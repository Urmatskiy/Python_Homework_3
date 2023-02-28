# Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

n = int(input("Введите количество чисел в списке: "))
x = int(input("Какое число ищем? "))

list_1 = list()

for i in range(n):
    list_1.append(random.randint(1, n))

print(*list_1)

if x in list_1:
    print(f"{x} уже есть в заданном списке")
else:
    result = abs(list_1[0] - x)
    result_digit = list_1[0]
    for i in range(len(list_1)):
        if abs(list_1[i] - x) < result:
            result = abs(list_1[i] - x)
            result_digit = list_1[i]
    print(f"{result_digit} - ближайшее число к {x}")
