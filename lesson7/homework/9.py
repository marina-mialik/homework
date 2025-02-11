'''
*
В структуре данных из 5 урока задание №2 каждому сотруднику 
добавить к параметру "навык" параметр "мастерство" измеряемый от 0 до 100

Написать программу которая анализирует всю структуру данных и выводит сотрудников
с наибольшим параметром "мастерство" для каждого существующего навыка.
Пример вывода:
    1. Python - Иванов - 98
    2. JS - Петров  - 74     
    3. Базы данных - Николаев - 87     
    ...


** Пример вывода (перед выводам отсортировать по убыванию "мастерства"):
    
    --------------------------------------------------
    | № |   Навык     |       ФИО       | Мастерство |
    ==================================================
    | 1 | Python      | Иванов Н.С.     |     98     |
    | 2 | JS          | Петров В.В.     |     87     |
    | 3 | Базы данных | Николаев Е.Н.   |     74     |
    ...

'''

employees = {
    "1": {
        "fullname": "Иванов Иван Иванович",
        "position": "Дизайнер",
        "birthday": 1992,
        "skills": [
            { "skill_name": "Illustrator", "mastery": 65 },
            { "skill_name": "Corel Draw", "mastery": 80 },
            { "skill_name": "Photoshop", "mastery": 40 },
        ],
        "children": [
            {"name": "Вероника", "birthday": 2017},
            {"name": "Михаил", "birthday": 2020},
        ],
    },
    "2": {
        "fullname": "Петров Петр Петрович",
        "position": "Юрист",
        "birthday": 2000,
        "skills": [
            { "skill_name": "Exel", "mastery": 65 },
            { "skill_name": "Word", "mastery": 80 },
            { "skill_name": "Консультант Плюс", "mastery": 40 },
            { "skill_name": "Английский", "mastery": 40 },
        ],
        "children": [
            {"name": "Лидия", "birthday": 2022},
        ],
    },
    "3": {
        "fullname": "Сидоров Василий Владимирович",
        "position": "Программист",
        "birthday": 1990,
        "skills": [
            { "skill_name": "Python", "mastery": 32 },
            { "skill_name": "JavaScript", "mastery": 54 },
            { "skill_name": "Django", "mastery": 44 },
            { "skill_name": "Git", "mastery": 90 },
        ],
        "children": [
            {"name": "Мария", "birthday": 2013},
        ],
    }   
}

workers = []

for worker in employees.values():
    first_name, second_name, middle_name = worker["fullname"].split()
    name = f"{second_name} {first_name[0]}.{middle_name[0]}."
    top_skill_name = ""
    top_mastery = 0

    for skill in worker["skills"]:
        skill_name, mastery = skill["skill_name"], skill["mastery"]

        if mastery >= top_mastery:
            top_mastery = mastery
            top_skill_name = skill_name
    
    result = {}
    result["skill"] = top_skill_name
    result["mastery"] = top_mastery
    result["name"] = second_name
    workers.append(result)

for idx, worker in enumerate(workers):
    print(f"{idx + 1}. {worker["skill"]} - {worker["name"]} - {worker["mastery"]}")