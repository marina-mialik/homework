"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""

import re
from datetime import datetime, timedelta
import random
import string

class User:
    def __init__(self, name: str, login: str, password: str = None):
        self.name = name
        self.login = login
        self.is_blocked = False
        self.subscription_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        self.subscription_mode = "free"

        if password is None:
            self.password = self._generate_password()
            print(f"Сгенерированный пароль: {self.password}")
        else:
            self.password = password

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not re.match(r'^[а-яА-ЯёЁ]+$', value):
            raise ValueError("Имя должно содержать только буквы русского алфавита!")
        self._name = value

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, value: str):
        if not re.match(r'^[a-zA-Z0-9_]{6,}$', value):
            raise ValueError("Логин должен быть не менее 6 символов, содержать только латинские буквы, цифры и подчеркивание")
        self._login = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str):
        if len(value) >= 6:
            raise ValueError("Пароль должен содержать менее шести символов.")
        if not re.search(r'[a-z]', value):
            raise ValueError("Пароль должен содержать хотя бы одну строчную букву.")
        if not re.search(r'[A-Z]', value):
            raise ValueError("Пароль должен содержать хотя бы одну заглавную букву.")
        if not re.search(r'[0-9]', value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру.")
        if not re.match(r'^[a-zA-Z0-9]+$', value):
            raise ValueError("Пароль должен содержать только латинские буквы и цифры.")
        self._password = value

    @property
    def subscription_date(self) -> str:
        return self._subscription_date

    @subscription_date.setter
    def subscription_date(self, value: str):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата подписки должна быть в формате YYYY-MM-DD.")
        self._subscription_date = value
        self.subscription_mode = "paid"

    @property
    def subscription_mode(self) -> str:
        return self._subscription_mode

    @subscription_mode.setter
    def subscription_mode(self, value: str):
        if value not in ["free", "paid"]:
            raise ValueError("Вид подписки должен быть 'free' или 'paid'.")
        self._subscription_mode = value

    def block(self, is_blocked: bool):
        if not isinstance(is_blocked, bool):
            raise ValueError("Аргумент должен быть булевым значением.")
        self.is_blocked = is_blocked

    def check_subscr(self, check_date: str = None):
        if check_date is None:
            check_date = datetime.now().strftime("%Y-%m-%d")

        try:
            check_date = datetime.strptime(check_date, "%Y-%m-%d")
            sub_date = datetime.strptime(self.subscription_date, "%Y-%m-%d")
        except ValueError:
            return "Неверный формат даты."

        if check_date > sub_date:
            return "Подписка не действует."

        days_left = (sub_date - check_date).days
        return f"Подписка действует. Вид: {self.subscription_mode}. Осталось дней: {days_left}."

    def change_pass(self, new_password: str = None):
        if new_password is None:
            new_password = self._generate_password()
            print(f"Сгенерированный пароль: {new_password}")
        self.password = new_password

    def _generate_password(self):
        while True:
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
            if (re.search(r'[a-z]', password) and
                re.search(r'[A-Z]', password) and
                re.search(r'[0-9]', password)):
                return password

    def get_info(self):
        status = "заблокирован" if self.is_blocked else "активен"
        info = (f"Имя: {self.name}\n"
                f"Логин: {self.login}\n"
                f"Статус: {status}\n"
                f"Подписка: {self.subscription_mode} до {self.subscription_date}")
        if self.is_blocked:
            info += "\nПользователь заблокирован."
        return info

try:
    user = User(name="Марина", login="My_123")
    print(user.get_info())
    print(user.check_subscr())
    print()
    user.block(True)
    print(user.get_info())
    print()
    user.change_pass()
    print(user.get_info())

except ValueError as e:
    print(e)
    

    
