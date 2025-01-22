price = float(input("Введите цену закупки телефона: "))

selling_price = price * 1.30
discount_5 = selling_price * 0.95
discount_10 = selling_price * 0.90
discount_15 = selling_price * 0.85

print(f"Цена продажи (+30% к цене закупке): {selling_price:.2f} руб.")
print(f"Цена продажи со скидкой 5%: {discount_5:.2f} руб.")
print(f"Цена продажи со скидкой 10%: {discount_10:.2f} руб.")
print(f"Цена продажи со скидкой 15%: {discount_15:.2f} руб.")