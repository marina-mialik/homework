'''
Программа должна запросить несколько цифр через пробел 
    - выдать их общую сумму
    - выдать максимальную цифру
    - выдать среднее арифметическое

'''

numbers = list(map(int, input().split()))

total_sum = sum(numbers)

max_value = max(numbers)

average = total_sum / len(numbers)

print("Общая сумма:", total_sum)
print("Максимальная цифра:", max_value)
print("Среднее арифметическое:", average)