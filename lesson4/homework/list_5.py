'''
Дан список
['samsung', 'lg', 'xerox', 'bosch']
Удалить элемент с именем 'xerox'
Добавить элемент на 2 место 'indesit'

'''

my_list = ['samsung', 'lg', 'xerox', 'bosch']

my_list.remove('xerox')

my_list.insert(1, 'indesit')

print("Измененный список:", my_list)