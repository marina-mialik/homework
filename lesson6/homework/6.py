"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""

a1, a2, a3, a4 = 1, 35, "task", 8.0

condition1 = all(isinstance(x, float) for x in [a1, a2, a3, a4])

condition2 = any(isinstance(x, str) for x in [a1, a2, a3, a4])

pairs = [
    (a1, a3),
    (a2, a4),
    (a3, a4)
    ]

condition3 = any(isinstance(x, int) and isinstance(y, int) for x, y in pairs)

print(condition1, condition2, condition3, sep = "\n")
