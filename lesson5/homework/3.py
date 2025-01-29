"""
дан словарь
d = {'one':11, 'two':22, 'hello':'python', True:False}
запросить номер элемента и удалить его из словаря с помощью del.

"""

d = {'one':11, 'two':22, 'hello':'python', True:False}

element = input("Введите номер элемента для удаления: ")

keys_list = list(d.keys())

del d[keys_list[int(element)]] # удаление по индексу
# del d[element] - удаление по ключу

print(d)

