"""

Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты(свойства):
    - value - текущее значение счетчика
    ...

Определить методы:
    - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
    - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
    - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
    - reset, сбрасывает значение счетчика на стартовое    
    - метод __iter__
    - метод __next__
    
    * - stat, возвращает среднее количество изменений счетчика в секунду

"""
# import time

# class Counter:
#     def __init__(self, start_value: int = 0, min_value: int = -float('inf'), max_value: int = float('inf')):
#         self._value = start_value
#         self._start_value = start_value
#         self._min_value = min_value
#         self._max_value = max_value
#         self._changes = 0
#         self._start_time = time.time()

#     @property
#     def value(self) -> int:
#         return self._value

#     def increase(self, num: int = 1):
#         self._value = min(self._value + num, self._max_value)
#         self._changes += 1

#     def decrease(self, num: int = 1):
#         self._value = max(self._value - num, self._min_value)
#         self._changes += 1

#     def reset(self):
#         self._value = self._start_value
#         self._changes += 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self._value >= self._max_value:
#             raise StopIteration
#         self.increase()
#         return self._value

#     def stat(self) -> float:
#         elapsed_time = time.time() - self._start_time
#         return self._changes / elapsed_time if elapsed_time > 0 else 0

# counter = Counter(start_value=5, min_value=0, max_value=10)

# print("Текущее значение:", counter.value)

# counter.increase(3)
# print("После увеличения на 3:", counter.value)

# counter.decrease(2)
# print("После уменьшения на 2:", counter.value)

# counter.reset()
# print("После сброса:", counter.value)

# print("Итерация:")
# for value in counter:
#     print(value, end=" ")
# print()

# print("Среднее количество изменений в секунду:", counter.stat())


import time

class Counter:
    def __init__(self, start_value: int = 0, min_value: int = -float('inf'), max_value: int = float('inf')):
        self._value = start_value
        self._start_value = start_value
        self._min_value = min_value
        self._max_value = max_value
        self._changes = 0
        self._start_time = time.time()

    def get_value(self) -> int:
        return self._value

    def increase(self, num: int = 1):
        self._value = min(self._value + num, self._max_value)
        self._changes += 1

    def decrease(self, num: int = 1):
        self._value = max(self._value - num, self._min_value)
        self._changes += 1

    def reset(self):
        self._value = self._start_value
        self._changes += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._value >= self._max_value:
            raise StopIteration
        self.increase()
        return self._value

    def stat(self) -> float:
        elapsed_time = time.time() - self._start_time
        return self._changes / elapsed_time if elapsed_time > 0 else 0

counter = Counter(start_value=3, min_value=0, max_value=20)

print("Текущее значение:", counter.get_value())

counter.increase(2)
print("После увеличения:", counter.get_value())

counter.decrease(1)
print("После уменьшения:", counter.get_value())

counter.reset()
print("После сброса:", counter.get_value())

print("Итерация:")
values = [value for value in counter]
print(" ".join(map(str, values)))

print("Среднее количество изменений в секунду:", counter.stat())