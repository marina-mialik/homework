"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""

from datetime import date

CURRENT_YEAR = date.today().year

class BookCard:
    def __init__(self, author: str, title: str, year: int):
        self.author = author
        self.title = title
        self.year = year

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Автор должен быть строкой.")
        self.__author = value

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Название книги должно быть строкой.")
        self.__title = value

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Год издания должен быть целым числом.")
        if value <= 0 or value > CURRENT_YEAR:
            raise ValueError(f"Год издания должен быть больше 0 и не больше {CURRENT_YEAR}.")
        self.__year = value

    def __eq__(self, other):
        if not isinstance(other, BookCard):
            return NotImplemented
        return self.year == other.year
    
    def __lt__(self, other):
        if not isinstance(other, BookCard):
            return NotImplemented
        return self.year < other.year

    def __le__(self, other):
        if not isinstance(other, BookCard):
            return NotImplemented
        return self.year <= other.year

    def __gt__(self, other):
        if not isinstance(other, BookCard):
            return NotImplemented
        return self.year > other.year
    
    def __ge__(self, other):
        if not isinstance(other, BookCard):
            return NotImplemented
        return self.year >= other.year

    def __str__(self):
        return f"BookCard(author={self.author}, title={self.title}, year={self.year})"
    
book1 = BookCard("Роберт Мартин", "Чистый код", 2019)
book2 = BookCard("Адитья Бхаргава", "Грокаем алгоритмы", 2022)
book3 = BookCard("Стив Макконнелл", "Совершенный код", 2017)

print(book1.author)
print(book2.title)
print(book2.year)
print(book3.year)

try:
    print(book1.__author)
except AttributeError as e:
    print(e)

books = [book1, book2, book3]
sorted_books = sorted(books)
for book in sorted_books:
    print(book)

try:
    book1.year = CURRENT_YEAR + 1
except ValueError as e:
    print(e)
