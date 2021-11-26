# Инициализация кортежа
sample = tuple() # Пустой кортеж
print("Len:", len(sample))
print("Type:", type(sample))

# Кортеж с элементами
sample = ("a", "b", "c", "d")
print("Len:", len(sample))
print("Sample:", sample)

# Фокус - кортеж из одного элемента
ones = (1,) # Преобразование списка в кортеж
print("Type:", type(ones), ones)

# Индексы и итерируемость
sample = ("a", "bb", "cc", "ddd")
print(sample[-1])
print(sample[0])
print(sample[0:3])

for i in range(len(sample)):
    print(i, sample[i])

for elem in sample:
    print(elem)

# Проверка вхождения
if "ddd" in sample:
    print("ddd in sample")


# Многомерная коллекция
multi_tuple = ([1,2,3,4], ["a", "b", "c", "d"], set([10, 20, 30]))
print("Len:", len(multi_tuple))

for coll_in_tuple in multi_tuple:
    out = ""
    for elem in coll_in_tuple:
        out += str(elem) + " "
    print(out)

# Индексация многомерных коллекция
multi_tuple[0][1]
coordinates = ((1, 2), (2, 3), (3, 4))

# Неизменяемость
sample = (1,2,3,4,5)
# sample[0] = 99999999  # Невозможно изменить ЗНАЧЕНИЕ элемента кортежа!!!!!!  

# Сравнение кортежей
print((1,2,3) < (4,5))

# Сравнение списков
print([1,2,3] < [4,5])