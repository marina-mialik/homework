'''
Дан список [1,2,3,4,5,6,7,8,9]. Создать 3 копии этого списка 
и с каждой выполнить след действия:
    - возвести каждый элемент во 2ю степень
    - прибавить 3 к каждому элементу значение которого является четным 
    - элементы значения которого является 
            четными - умножить на 2 
            нечетным - умножить на 3

Использовать map и lambda.
'''

list_numbers = [1,2,3,4,5,6,7,8,9]

mapped_list1 = list(map(lambda n: n**2, list_numbers))
mapped_list2 = list(map(lambda n: n + 3 if n % 2 == 0 else n, list_numbers))
mapped_list3 = list(map(lambda n: n * 2 if n % 2 == 0 else n * 3, list_numbers))

print(mapped_list1)
print(mapped_list2)
print(mapped_list3)
