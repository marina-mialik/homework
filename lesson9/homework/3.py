
'''
Написать рекурсивную функцию, которая принимает 2 аргумента 
(целые числа - a и b) и высчитывает суммы всех чисел от a до b (включительно). 
Пример: a = 3, b = 5 -> 12 (3+4+5)
Пример: a = 5, b = 9 -> 35 (5+6+7+8+9)"

'''

def get_sum(a: int, b: int) -> int:
    if a < 0 or b < 0:
        raise ValueError("Значение не может быть отрицательным!")

    if isinstance(a, (float, str)) or isinstance(b, (float, str)):
        raise TypeError("Значение должно быть только целым числом!")
    
    if a > b:
        raise ValueError("Начальное число (a) не может быть больше конечного (b)")

    if a == b:
        return a

    return a + get_sum(a + 1, b)

try:
    print(get_sum(5, 9))
    print(get_sum(1, 9))
    print(get_sum(-5, 9))
    print(get_sum(5, -9))
    print(get_sum("5", 9))
    print(get_sum(5, "9"))
    print(get_sum(5, 9.1))
    print(get_sum(5.8, 9))
except ValueError as e:
    print("Ууупс... Что-то пошло не так с Вашим числом.", e)
except TypeError as e:
    print("Ууупс... Что-то пошло не так с типом Вашего числа.", e)
