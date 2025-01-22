num_seconds = int(input("Введите количество секунд: "))

hours = num_seconds // 3600
minutes = (num_seconds % 3600) // 60
seconds = num_seconds % 60

formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

# без форматной строки
# formatted_time = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

print(formatted_time)