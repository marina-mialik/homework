"""
*
Написать программу калькулятор которая предлагает 
ввести пример для решения пока пользователь не введет команду "стоп"
Программа должна решить пример и запросить следующий.
При вводе команды "стоп" программа завершается.
Поддерживаемые операции: + - * ** /
Пример:
    Введите пример или 'стоп' для завершения: 2 + 2
    Ответ: 4
    Введите пример или 'стоп' для завершения: 16 / 8
    Ответ: 2
    Введите пример или 'стоп' для завершения: 1651+
    Неправильный формат. Пример: '2 + 4'

"""

operations = {
    'sum': "+",
    'sub': "-",
    'mul': "*",
    'div': "/",
    'pow': "**"
}

def set_warnings(a: str | None, b: str | None, operation: str) -> str:
    if not a or not b:
        return f"Неправильный формат. Пример: '2 {operation} 4'."
    
    a, b = a.replace('.', '', 1), b.replace('.', '', 1)

    if not a.isdigit() or not b.isdigit():
        return "Некорректные числа."
    
    return ""


def get_sum(a: str | None, b: str | None) -> str:
    warnings = set_warnings(a, b, operations['sum'])

    if len(warnings):
        return warnings

    a, b = int(a), int(b)
    return a + b

def get_sub(a: str | None, b: str | None) -> str:
    warnings = set_warnings(a, b, operations['sub'])

    if len(warnings):
        return warnings
    
    a, b = int(a), int(b)
    return a - b

def get_mul(a: str | None, b: str | None) -> str:
    warnings = set_warnings(a, b, operations['mul'])

    if len(warnings):
        return warnings

    a, b = int(a), int(b)
    return a * b

def get_div(a: str | None, b: str | None) -> str:
    warnings = set_warnings(a, b, operations['div'])

    if len(warnings):
        return warnings

    a, b = int(a), int(b)
    
    if b == 0:
        return 'На ноль делить нельзя'

    return a / b

def get_pow(a: str | None, b: str | None) -> str:
    warnings = set_warnings(a, b, operations['pow'])

    if len(warnings):
        return warnings

    a, b = int(a), int(b)
    return a ** b

while True:
    example = input("Введите пример или 'стоп' для завершения: ").replace(' ', '')

    if example.lower() == "стоп":
        break

    if operations['sum'] in example:
        a, b = example.split(operations['sum'])
        print(f"Ответ: {get_sum(a, b)}")
    elif operations['sub'] in example:
        a, b = example.split(operations['sub'])
        print(f"Ответ: {get_sub(a, b)}")
    elif operations['pow'] in example:
        a, b = example.split(operations['pow'])
        print(f"Ответ: {get_pow(a, b)}")
    elif operations['mul'] in example:
        a, b = example.split(operations['mul'])
        print(f"Ответ: {get_mul(a, b)}")
    elif operations['div'] in example:
        a, b = example.split(operations['div'])
        print(f"Ответ: {get_div(a, b)}")
    else:
        print("Неизвестная операция.")