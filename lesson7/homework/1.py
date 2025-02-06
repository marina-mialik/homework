"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.
"""

sum_marks = 0
count = 0

while True:
    mark = int(input("Введите оценку: "))
    if mark == 0:
        break
    sum_marks += mark
    count += 1

print(f"Средний балл: {sum_marks / count if count else 0}")