"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""

def yes_or_no(numbers: list) -> list:
    if not all(isinstance(num, int) for num in numbers):
        return []

    yes = "yes"
    no = "no"

    hach_set = set()
    result = []

    for num in numbers:
        if num in hach_set:
            result.append(yes)
        else:
            hach_set.add(num)
            result.append(no)

    return result

print(yes_or_no([1, 2, 3, 1, 4]))  
print(yes_or_no([1, 1, 1, 1, 1]))
print(yes_or_no([]))               
print(yes_or_no([1, "2", 3, 4]))    
print(yes_or_no([1, 2.5, 3, 4]))  
        

