"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""

dct = {
    "day1": 18,
    "day2": 22,
    "day3": 7,
    "day4": 11,
    "day5": 14
}

sorted_dct = dict(sorted(dct.items(), key=lambda item: item[1]))
sorted_dct2 = dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))

print("Сортировка по возрастанию:", sorted_dct)
print("Сортировка по убыванию:", sorted_dct2)
