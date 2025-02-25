"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: 
        <Бренд-Модель> - Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""

class Phone:
    def __init__(self, brand: str, model: str | int, issue_year: int):
        self.set_info(brand, model, issue_year)

    def __str__(self):
        return f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"

    def set_info(self, brand: str = None, model: str | int = None, issue_year: int = None):
        if brand is not None and not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        
        if model is not None and not isinstance(model, (str, int)):
            raise TypeError("Модель должна быть строкой или числом")
        
        if issue_year is not None and not isinstance(issue_year, int):
            raise TypeError("Год выпуска должен быть целым числом")
        
        if brand is not None:
            self.brand = brand

        if model is not None:
            self.model = str(model)

        if issue_year is not None:
            self.issue_year = issue_year

    def get_info(self) -> tuple:
        return self.brand, self.model, self.issue_year

    def receive_call(self, name: str):
        if not name:
            raise ValueError("Имя звонящего не может быть пустым")
        print(f"{self.brand}-{self.model} - Звонит {name}")

try:
    phone1 = Phone("Nokia", "3310", 2010)
    phone2 = Phone("iPhone", "2g", 2007)
    phone3 = Phone("Samsung", "sII", 2011)

    phone1.set_info(model="3311")

    phone1.receive_call("Apple")
    phone2.receive_call("Иван")

    print(phone3)
except (ValueError, TypeError) as e:
    print(f"Упс... Что-то пошло не так!: {e}")