# Задача D. Дни рождения (с динамичесим добавлением ключей)
dates = {}

n_friends = int(input().strip())

for _ in range(n_friends):
    message = input().strip() # "Вася 12 дек"
    name, _, month = message.split() # ["Вася", "12", "дек"]
    if month in dates.keys():
        dates[month].append(name)
    else:
        dates[month] = [name] # {"дек" : ["Петя" , "Вася"]}

n_months = int(input().strip())
for _ in range(n_months):
    curr_month = input().strip()
    names = dates[curr_month]

    if len(names) == 0:
        print()
    else:
        print(" ".join(sorted(names)))