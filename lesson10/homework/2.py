
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""

def factorial():
    result = 1
    counter = 1
    while True:
        yield result
        counter += 1
        result *= counter

factorial_gen = factorial()

print(next(factorial_gen)) #-> 1
print(next(factorial_gen)) #-> 2
print(next(factorial_gen)) #-> 6
print(next(factorial_gen)) #-> 24
