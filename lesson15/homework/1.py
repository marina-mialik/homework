"""
Используя класс из пред.урока обеспечить хранение и сохранение любых изменений в базе 
данных. Для этого можно к примеру добавить в класс метод save который будет сохранять или 
создавать пользователя в базе данных и использовать его при любых изменениях.


* в базе данных создать таблицу предоставляемых услуг со след полями
	название
	тип (1 - платная 0 - бесплатная)
	стоимость 
	период в днях
** в класс пользователя добавить методы:
	добавить услугу (услуг у одного пользователя может быть несколько)
	продлить услугу (продлить можно если услуга еще не закончена, иначе добавить)
	удалить услугу
*** создать консольное или оконное приложение которое показывает меню и отрабатывает выбранный пункт.
	Меню:
		1 - показать пользователей
		2 - информация о пользователе (в т.ч. и подключенные услуги)
		3 - список услуг		
		4 - показать пользователей с определенной услугой
		5 - показать пользователей у которых за прошедший месяц окончился период хоть одной услуги 
"""

# brew services start mongodb-community@8.0 - Запуск MongoDB
# brew services stop mongodb-community@8.0 - Отключение MongoDB
# source path/to/env/bin/activate - Активация виртуального окружения
# deactivate - Выклюение виртуального окружения

from pymongo import MongoClient
import re
from datetime import datetime, timedelta
import random
import string

client = MongoClient('localhost', 27017)
db = client.user_credentials
users = db.users

class User:
	def __init__(self, name: str, login: str, password: str = None):
		# Проверка уникальности логина
		if users.find_one({"login": login}):
			raise ValueError("Пользователь с таким логином уже существует!")

		self._name = name
		self._login = login
		self._subscription_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
		self._subscription_mode = "free"
		self.is_blocked = False
		self.services = []

		if password is None:
			self.password = self._generate_password()
			print(f"Сгенерированный пароль: {self.password}")
		else:
			self.password = password

		self.save()

	@property
	def name(self) -> str:
		return self._name

	@name.setter
	def name(self, value: str):
		if not re.match(r'^[а-яА-ЯёЁ]+$', value):
			raise ValueError("Имя должно содержать только буквы русского алфавита!")
		self._name = value
		self.save()

	@property
	def login(self) -> str:
		return self._login

	@login.setter
	def login(self, value: str):
		if not re.match(r'^[a-zA-Z0-9_]{6,}$', value):
			raise ValueError("Логин должен быть не менее 6 символов, содержать только латинские буквы, цифры и подчеркивание")
		self._login = value
		self.save()

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
		self.save()

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
		self.save()

	@property
	def subscription_mode(self) -> str:
		return self._subscription_mode

	@subscription_mode.setter
	def subscription_mode(self, value: str):
		if value not in ["free", "paid"]:
			raise ValueError("Вид подписки должен быть 'free' или 'paid'.")
		self._subscription_mode = value
		self.save()

	def block(self, is_blocked: bool):
		if not isinstance(is_blocked, bool):
			raise ValueError("Аргумент должен быть булевым значением.")
		self.is_blocked = is_blocked
		self.save()

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
		self.save()

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

	def add_service(self, service_name: str, service_type: int, cost: float, period: int):
		if service_type not in [0, 1]:
			raise ValueError("Тип услуги должен быть 0 (бесплатная) или 1 (платная).")

		service = {
			"name": service_name,
			"type": service_type,
			"cost": cost,
			"period": period,
			"start_date": datetime.now().strftime("%Y-%m-%d"),
			"end_date": (datetime.now() + timedelta(days=period)).strftime("%Y-%m-%d")
		}
		self.services.append(service)
		self.save()

	def extend_service(self, service_name: str, period: int):
		for service in self.services:
			if service["name"] == service_name:
				if datetime.strptime(service["end_date"], "%Y-%m-%d") > datetime.now():
					service["end_date"] = (datetime.strptime(service["end_date"], "%Y-%m-%d") + timedelta(days=period)).strftime("%Y-%m-%d")
					self.save()
					return
				else:
					self.add_service(service_name, service["type"], service["cost"], period)
					return
		raise ValueError("Услуга не найдена.")

	def remove_service(self, service_name: str):
		self.services = [service for service in self.services if service["name"] != service_name]
		self.save()
	
	def save(self):
		print(self.login)
		user_data = {
		    "name": self.name,
		    "login": self.login,
		    "password": self.password,
		    "is_blocked": self.is_blocked,
		    "subscription_date": self.subscription_date,
		    "subscription_mode": self.subscription_mode,
		    "services": self.services
		}
		users.update_one({"login": self.login}, {"$set": user_data}, upsert=True)

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

	user.add_service("Премиум подписка", 1, 50, 30)
	print(user.get_info())

	user.extend_service("Премиум подписка", 30)
	print(user.get_info())

	user.remove_service("Премиум подписка")
	print(user.get_info())

except ValueError as e:
	print(e)

print(users.find_one({ "login": "My_123" }))