'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.

'''

data = [
    42,
    "Hello",
    "Python",
    3.14,
    "Hi",
    "Data Science",
    [1, 2, 3],
    {"name": "John"},
    "AAA",
    "Machine Driving",
    True,
    "OpenCode"
]

strings_data = list(filter(lambda string: isinstance(string, str), data))
bools_data = list(filter(lambda string: isinstance(string, bool), data))

print("Строки:", strings_data)
print("Логический тип:", bools_data)
