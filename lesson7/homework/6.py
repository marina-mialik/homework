"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""

reviews = {}

while True:
    name = input("Введите ваше имя (или 'stop' для завершения): ")
    if name.lower() == "stop":
        break

    review = input("Введите ваш отзыв: ")
    reviews[name] = review

print(f"Количество отзывов: {len(reviews)}")

print("Имена пользователей:")
for key in reviews.keys():
    print(f"{key}")
    
print("Отзывы пользователей:")
for value in reviews.values():
    print(f"{value}")