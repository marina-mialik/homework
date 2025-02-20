'''
*
Написать рекурсивную функцию, которая принимает список 
и печатает каждых элемент на новой строке. 
Если элемент списка - список, то его элементы должны выводиться 
с отступом относительно родительского на 2 символа. 
Символ для отступа передать дополнительными необязательным параметром.

** написать такую же функцию но без рекурсии

Пример1: some_list = [1, 2, 3, [4, [5, 6], 7], 8, 9]
1
2
3
--4
----5
----6
--7
8
9

Пример2: some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]
1
--2
------3
----4
5
------6
------7
8
--------9
--------10
----11
12

'''

def get_list_view(deep_list, padding="-"):
    stack = []

    for item in reversed(deep_list):
      stack.append((item, 0))
    
    while stack:
      item, level = stack.pop()

      if isinstance(item, list):
        for element in reversed(item):
          stack.append((element, level + 1))
      else:
        shifted_padding = padding * 2 * level
        print(f"{shifted_padding}{item}")
  
def get_list_view_recursion(lst: list, padding="-"):
    if not len(lst):
        raise ValueError("Значение lst не может быть пустым!")

    if not len(padding):
        raise ValueError("Значение padding не может быть пустое!")

    updated_padding = "" if len(padding) == 1 else padding
    shifted_padding = updated_padding + (padding[0] * 2)

    for item in lst:
        if isinstance(item, list):
            get_list_view_recursion(item, shifted_padding)
        else:   
            print(updated_padding, item, sep = "")

some_list=[1,[2,[[3],4]],5,[[[6,7]]],8,[[[[9,10]],11]],12]
empty_list = []
empty_nested_list = [[]]
some_padding = "*"
empty_padding = ""

try:
    get_list_view(some_list)
    get_list_view_recursion(some_list)
    print('===========')
    get_list_view_recursion(some_list, padding=some_padding)
    print('===========')
    get_list_view_recursion(empty_nested_list)
    print('===========')
    get_list_view_recursion(some_list, padding=empty_padding)
    print('===========')
    get_list_view_recursion(empty_list)
    print('===========')
    get_list_view_recursion(empty_list, padding=some_padding)
    print('===========')
    get_list_view_recursion(empty_list, padding=empty_padding)
except ValueError as e:
    print("Упс... Что-то пошло не так.", e)
