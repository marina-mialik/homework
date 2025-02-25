"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""

class Student:
    def __init__(self, surname: str, name: str, group: str | int, grads: list[int]):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads

    def __str__(self):
        return f"{self.surname} {self.name}"

    def add_grade(self, *grades: int):
        for grade in grades:
            if not (1 <= grade <= 10):
                raise ValueError("Оценка должна быть от 1 до 10")
        self.grads.extend(grades)

    def average_grade(self) -> float:
        if not self.grads:
            return 0
        return sum(self.grads) / len(self.grads)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

students = [
    Student("Ivanov", "Ivan", 11, [9, 5, 8, 10, 7]),
    Student("Petrov", "Petr", "9A", [9, 3, 8, 2, 7]),
    Student("Sidorov", "Gleb", 6, [2, 7, 3, 8, 7, 5]),
    Student("Kuznetsova", "Anna", 10, [10, 8, 9]),
    Student("Smirnov", "Dmitriy", "10B", [3, 6, 4, 7, 7])
]

sorted_students_asc = sorted(students)
print("По возрастанию:", list(map(str, sorted_students_asc)))

sorted_students_desc = sorted(students, reverse=True)
print("По убыванию:", list(map(str, sorted_students_desc)))

best_students = [student for student in students if student.average_grade() > 8]
print("Средний балл больше 8:", list(map(str, best_students)))
