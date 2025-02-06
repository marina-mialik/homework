'''
Запросить любое число. Заменить каждую цифру этого числа буквой, 
у которой номер в алфавите равен этой цифре. 
Например: 1352=aceb.
'''

number = input("Введите число: ")
result = ''.join(chr(ord('a') + int(digit) -1) for digit in number)
print(result)