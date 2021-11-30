## Лекция 16. Словари

**Словарь** (dict) - это множество **ПАР** вида `key`:`value`.

### 1. Инициализация
```
## Инициализация пустого словря
birthdays = {} #  Словарь дней рождений
print("Len:", len(birthdays), "Type:", type(birthdays))

sample = dict() # Инициализация через конструктор (тоже пустой)
```

### 2. Для чего нужен словарь и как добавить значения?
```
# Инициализация пустой/с элементами
translator = {} # dict() - пустой
translator = {"cat" : "кошка", "dog" : "песик", "milk" : "молоко"} # Инициализация с элементами

print("Translator:", translator)
print("Len:", len(translator))
print("Type:", type(translator))

# Обращение к элементам и добавление новых
print("By key cat:", translator["cat"]) # Обращение к существующему
#print("By key tea:", translator["tea"]) # Обращение к НЕсуществующему

translator["tea"] = "чай" # dict[new_key] = new_value
print("By key tea:", translator["tea"])
print("Len:", len(translator))

# Перезапись в словаре
translator["cat"] = "кот"
translator["dog"] = "пес"

print(translator)
```
* Требования к ключам
```
# Ключами в словаре могут быть какие угодно **сравнимые** типы данных
d = {
    True: "yes",
    None: "no",
    3 : "second",
    "index" : "third",
    24.5 : "bob",
    (10,20) : "alex",
    3 : "SECOND"
    # [10, 20, 30] : "den",
}


print(d)
```
Ключ в словаре - это любой элемент, который удовлетворяет слуд.условиям:
* 1) Этот элемент - представитель НЕИЗМЕНЯЕМОГО ТИПА!!!!
* 2) Ключ должны быть уникальными!

* Требования к значениям:
1) Значения могут быть совершенно любые!


* Пример использования словаря как хранилище:
```
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
```

* Проверка вхождения ключа:
```
# Проверка наличия ключа
translator = {"cat" : "кот", "dog" : "пес"}

new_key = "жираф"

# Проверка вхождения ключа:
if new_key in translator.keys(): # Идет только проверка в ключах!
    print(f"{new_key} in translator keys")
else:
    print(f"{new_key} not in translator keys")


# Перебор ключей словаря
for k in translator.keys():
    print("Key:", k)
```

* Проверка значения
```
# Посмотреть на значения
if "кот" in translator.values():
    print("YES")


for v in translator.values():
    print("Val:", v)
```

* Перебор элементов словаря:
```
# Перебор элементов
for elem in translator:
    print(elem, translator[elem])

# Метод .items()
for k, v in translator.items(): # -> (("cat", "кот"), ("dog", "пес"))
    print("Key:", k, "Val:", v)
```

* Не упорядоченность словарей определяется тем, что невозможно четко сформулировать правло сравнения ключей!
```
d = {1 : "one", 1.01: "one dot zero one", "1" : "one str"}

for k, v in d.items(): # (1, "one"), (1.01, "one dot.."), ("1", "one_str")
    print(k, v)

for k in d:
    print(k, d[k])
print(d.items())
```

* Удаление элементов из словаря
```
# Удаление элементов (выполняется только по ключу), т.е. удаление пары
translator = {"cat" : "кот", "dog" : "пес"}
del translator["dog"] # None

print(translator)
```