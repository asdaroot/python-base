# Задача D. Дни рождения
dates = {
    "янв" : [],
    "фев" : [],
    "мар" : [],
    "апр" : [],
    "май" : [],
    "июн" : [],
    "июл" : [],
    "авг" : [],
    "сен" : [],
    "окт" : [],
    "ноя" : [],
    "дек" : [],
}

n_friends = int(input().strip())

for _ in range(n_friends):
    message = input().strip() # "Петя 12 дек"
    name, _, month = message.split() # ["Петя", "12", "дек"]
    dates[month].append(name)

n_months = int(input().strip())
for _ in range(n_months):
    curr_month = input().strip()
    names = dates[curr_month]

    if len(names) == 0:
        print()
    else:
        print(" ".join(sorted(names)))