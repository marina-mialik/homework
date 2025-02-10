'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''
SQUARE = "square"
PERIMETER = "perimeter"

def get_square(a: float, b: float) -> float:
    return a * b 

def get_perimeter(a: float, b: float) -> float:
    return 2 * (a + b)

def get_square_or_perimeter(a: float, b: float, action: str = SQUARE) -> float:
    if a <= 0 or b <= 0:
        raise ValueError("Стороны должны быть положительными числами")
    
    is_square = action == SQUARE
    return get_square(a, b) if is_square else get_perimeter(a, b)

a, b = input("Введите 2 числа через пробел: ").split()
print(get_square_or_perimeter(float(a), float(b)))
print(get_square_or_perimeter(float(a), float(b), SQUARE))
print(get_square_or_perimeter(float(a), float(b), PERIMETER))