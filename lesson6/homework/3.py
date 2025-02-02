'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))

if number1 > number2 and number1 > number3:
    max_number = number1
elif number2 > number1 and number2 > number3:
   max_number = number2
else:
    max_number = number3

print("Наибольшее число:", max_number)