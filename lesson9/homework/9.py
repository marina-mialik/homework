"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    if all(isinstance(arg, int) for arg in args):
        sum_of_args = sum(args)
    else:
        raise TypeError("Все позиционные аргументы должны быть целыми")

    if all(isinstance(value, str) for value in kwargs.values()):
        max_length = 0
        for value in kwargs.values():
            max_length = max(max_length, len(value))
    else:
        raise TypeError("Все аргументы - ключевые слова должны быть строками")

    return {"sum": sum_of_args, "max_length": max_length}


try:
    result = dict_from_args(1, 2, 3, 4, name="some_name", login="some_login", password="some_password")
    print(result) 

    result = dict_from_args(10, 20, 30, name="some", login="some_login")
    print(result)

    result = dict_from_args(1, 2, "3", 4, name="some_name", login="some_login", password="some_password")
    print(result)
except TypeError as e:
    print(e)

try:
    result = dict_from_args(1, 2, name="some", login=4567)
    print(result)
except TypeError as e:
    print(e)
