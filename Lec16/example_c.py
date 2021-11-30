# Пример
birthdays = {"янв" : [], "фев" : [], "мар" : []}

# Буду вводить строки вида "<месяц> <день>"
# Задча - правильно разложить по словарю

while True:
    message = input()
    if message == "" :
        break
    month, day_str = message.split() # ["янв", "31"]
    birthdays[month].append(int(day_str))

    print(birthdays)