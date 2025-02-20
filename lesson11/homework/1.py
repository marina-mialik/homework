"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""

def error_logger(log_console=True, log_file=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                error_message = f"Ошибка в функции {func.__name__}: {e}"

                if log_console:
                    print(error_message)

                if log_file:
                    with open(log_file, "a", encoding="utf-8") as file:
                        file.write(error_message + "\n")

        return wrapper
    return decorator


@error_logger(log_console=True, log_file="errors.log")
def divide(a, b):
    return a / b

divide(10, 0)
