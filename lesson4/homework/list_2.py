'''
Запросить по очереди у пользователя 5 имен. Добавить все в список. 
Отсортировать. 
Вывести на экран.
Вывести True при наличии в списке имени 'Вася'
'''

names = []

for i in range(5):
  name = input()
  names.append(name)

names.sort()
print(names)

vasya = 'Вася' in names
print("Содержит ли список имя 'Вася':", vasya)