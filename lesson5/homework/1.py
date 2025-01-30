"""
Запросить трижды ввод наименования товаров и их цену через пробел. 
"пример: 
>>>яблоко 10"
>>>груша 15
>>>малина 20
    
    - создать из введенных данных словарь где ключ это наименование, а цена значение
    - запросить имя товара, найти его в словаре, и вывести его цену, увеличенную на 15%. 
    - вывести сумму всех товаров

"""

products = {} 

for i in range(3):
     x = input()
     product, price = x.split()
     products[product] = int(price)

name_product = input()

increased_price = products[name_product] * 1.15
print(f"Цена {name_product} с увеличением 15%: {increased_price:.2f}")
      
print(sum(products.values()))

