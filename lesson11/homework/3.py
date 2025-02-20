"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""

def bread_dec(func):
    def inner(*args):
        print("</------------\\>")
        func(*args)
        print("<\\____________/>")

    return inner

def tomato_dec(func):
    def inner(*args):
        print("*** помидоры ****")
        func(*args)

    return inner

def salad_dec(func):
    def inner(*args):
        print("~~~~ салат ~~~~~")
        func(*args)

    return inner

def cheese_dec(func):
    def inner(*args):
        print("^^^^^ сыр ^^^^^^")
        func(*args)

    return inner

def onion_dec(func):
    def inner(*args):
        print("----- лук ------")
        func(*args)

    return inner

def get_beef():
    print("### говядина ###")

def get_chicken():
    print("|||| курица ||||")

@bread_dec
@onion_dec
@tomato_dec
def get_hamburger():
    get_beef()

@bread_dec
@cheese_dec
@salad_dec
def get_cheeseburger():
    get_chicken()

print("Гамбургер:")
get_hamburger()
print()
print("Чикенбургер:")
get_cheeseburger()
