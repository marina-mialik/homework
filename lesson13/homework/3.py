"""
в файле hero1 добавить следующий функционал
        - добавить несколько классов других героев унаследовав их от Hero.
        - Каждому герою добавить уникальное свойство-спец.очки (мана, ярость, и т.п. ) и 
                и свойство cо значением урона от спец.атаки.
        - Создать метод атаки special_attack которая возможна только если количество 
                спец.очков более 0.
        - Добавить метод attack который при атаке с вероятностью 25% будет использовать 
                спец.способность героя если у него остались спец.очки. 
                При спец атаке вычитать из очков 1. Если вероятность пришлась на
                остальные 75% - выполнить обычную атаку. Вывести сообщение в консоль 
                о типе и результате атаки.

добавить класс Arena:
        - атрибут warriors - все воины на арене (тип list)
        - магический метод __init__, который принимает необязательный аргумент warriors.
                Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
                пустым списком.
        - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
                Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
                Если нет, то добавить воина к списку warriors и вывести сообщение на экран
                "{warrior.name} участвует в битве"
        - метод choose_warrior, который не принимает аргументов и возвращает случайного
                воина из warriors
        - метод battle, который не принимает аргументов и симулирует битву. Сперва 
                должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
                исключение ValueError("Количество воинов на арене должно быть больше 1").
                Битва продолжается, пока на арене не останется только один воин. Сперва
                в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
                защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
                из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
                Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
                Вернуть данного воина из метода battle.
                
                
Создать несколько воинов используя разные классы, добавить их на арену и запустить битву. 
Выжить должен только один.

"""

from random import randint, choice

class Hero:
    def __init__(self, name: str, health: int, armor: int, power: int):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.points = 0
        self.special_power = 0

    def set_special_points(self, value: int = 0):
        self.points = value
    
    def set_special_power(self, value: int = 0):
        self.special_power = value

    def base_attack(self, other):        
        damage = self.power
        other.armor -= damage

        if other.armor < 0:
            other.health += other.armor
            other.armor = 0

        if other.health < 0:
            other.health = 0

    def special_attack(self, other):
        damage = self.power + self.special_power
        other.armor -= damage

        if other.armor < 0:
            other.health += other.armor
            other.armor = 0

        if other.health < 0:
            other.health = 0

    def attack(self, other):
        is_special = randint(1, 100) <= 25
        has_points = self.points > 0

        if is_special and has_points:
            print(f"{self.name} использует специальную атаку на {other.name}!")
            self.special_attack(other)
            self.points -= 1
        else:
            print(f"{self.name} атакует {other.name}!")
            self.base_attack(other)

        print(f"{other.name}: здоровье = {other.health}, броня = {other.armor}")

    def __str__(self) -> str:
        return (f"Name - {self.name}\n"
                f"Health - {self.health}\n"
                f"Armor - {self.armor}\n"
                f"Power - {self.power}\n"
                f"Points - {self.points}\n")

class Mage(Hero):
    def __init__(self):
        super().__init__("Mage", 6, 5, 8)
        self.set_special_points(10)
        self.set_special_power(4)
    
class Warrior(Hero):
    def __init__(self):
        super().__init__("Warrior", 10, 10, 4)
        self.set_special_points(4)
        self.set_special_power(2)

class Rogue(Hero):
    def __init__(self):
        super().__init__("Rogue", 8, 7, 6)
        self.set_special_points(6)
        self.set_special_power(3)


class Arena:
    def __init__(self, warriors: list = None):
        self.warriors = warriors if warriors is not None else []

    def add_warrior(self, warrior):
        if warrior in self.warriors:
            raise ValueError("Воин уже на арене")
        self.warriors.append(warrior)
        print(f"{warrior.name} участвует в битве")

    def choose_warrior(self):
        if not self.warriors:
            raise ValueError("На арене нет воинов")
        return choice(self.warriors)

    def battle(self):
        if len(self.warriors) < 2:
            raise ValueError("Количество воинов на арене должно быть больше 1")

        print("Начало битвы!")
        while len(self.warriors) > 1:
            attacker = self.choose_warrior()
            defender = self.choose_warrior()

            while defender == attacker:
                defender = self.choose_warrior()

            attacker.attack(defender)

            if defender.health <= 0:
                self.warriors.remove(defender)
                print(f"{defender.name} пал в битве")

        winner = self.warriors[0]
        print(f"Победил воин: {winner.name}")
        return winner

mage = Mage()
warrior = Warrior()
rogue = Rogue()

arena = Arena()
arena.add_warrior(mage)
arena.add_warrior(warrior)
arena.add_warrior(rogue)

try:
    winner = arena.battle()
except ValueError as e:
    print(e)
