"""
Запросить у пользователя год рождения и в соответствии с его возрастом 
охарактеризовать пользователя - 
ребенок, подросток, юноша, в расцвете сил, пожилой, старик.
"""

from datetime import datetime

year_of_birth = int(input("Введите Ваш год рождения: "))

current_year = datetime.now().year

age = current_year - year_of_birth

if age < 13:
    print("Вы ребенок.")
elif age < 18:
    print("Вы подросток.")
elif age < 30:
    print("Вы юноша.")
elif age < 60:
    print("Вы в расцвете сил.")
elif age < 75:
    print("Вы пожилой человек.")
else:
    print("Вы старик.")