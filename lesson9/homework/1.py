"""
Написать функцию print_n() которая будет печатать переданный текст, 
но при этом перед этим текстом выводить строку с номером отражающим 
кокай раз по счету выполняется эта функция. 

"""

# counter = 0

# def print_n(string: str):
#     global counter
#     counter += 1
#     print(counter, string)

# print_n("Hello")
# print_n("my")
# print_n("name")  
# print_n("is")
# print_n("Python")

def make_print_n():
    counter = 0
    def print_n(string: str):
        nonlocal counter
        counter += 1
        print(counter, string)
    return print_n

print_n = make_print_n()

print_n("Hello")
print_n("my")
print_n("name")
print_n("is")
print_n("Python")

