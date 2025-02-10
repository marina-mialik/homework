'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''

def get_factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Число должно быть положительное")
    if num == 0:
        return 1
    
    result = 1
    for n in range(1, num + 1):
        result *= n

    return result

data = int(input("Введите число: "))
factorial = get_factorial(data)
print(factorial)