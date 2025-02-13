'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''

def get_factorial(number: int) -> int:
    if not isinstance(number, int):
        raise TypeError("Факториал вычисляется только для целых чисел")
    if number < 0:
        raise ValueError("Значение не может быть меньше нуля!")

    return 1 if number <= 1 else number * get_factorial(number - 1)
    
try:
    print(get_factorial(0))
    print(get_factorial(1))
    print(get_factorial(5))
    print(get_factorial("10"))
    print(get_factorial(-5))
except ValueError as e:
    print("Упс... Что-то пошло нет.", e)
