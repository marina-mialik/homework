'''
Запросить 3 раза строку из нескольких чисел через пробел
    - вывести все уникальные числа по возрастанию
    - вывести числа которые есть в каждой строке
    -* вывести числа которые есть только в одной из трех строк
    
    выполнить без циклов и условий
    
    пример:
    >>> 1 2 11 22
    >>> 1 2 22 33
    >>> 1 2 33 44


    1) 1 2 11 22 33 44
    2) 1 2
    3) 11 44
    
'''

numbers1 = input("Введите числа через пробел: ")
numbers2 = input("Введите числа через пробел: ")
numbers3 = input("Введите числа через пробел: ")

set1 = set(map(int, numbers1.split()))
set2 = set(map(int, numbers2.split()))
set3 = set(map(int, numbers3.split()))

unique_numbers = sorted(set1 | set2 | set3)

popular_numbers = sorted(set1 & set2 & set3)

unique = sorted((set1 ^ set2 ^ set3))

print(f"1) {' '.join(map(str, unique_numbers))}")
print(f"2) {' '.join(map(str, popular_numbers))}")
print(f"3) {' '.join(map(str, unique))}")

