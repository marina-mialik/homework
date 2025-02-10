"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""

def get_initials(string: str, format=False) -> str:
    parts = string.split()
    if len(parts) != 3:
        raise ValueError("ФИО должно содержать: фамилию, имя и отчество")
    
    last_name, first_name, middle_name = parts
    initials = f"{first_name[0]}.{middle_name[0]}."
    
    return f"{initials}{last_name}" if format else f"{last_name} {initials}"

data = input()

print(get_initials(data))
print(get_initials(data, True))
