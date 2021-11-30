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


# Посмотреть на значения
if "кот" in translator.values():
    print("YES")


for v in translator.values():
    print("Val:", v)

# Перебор элементов
for elem in translator:
    print(elem, translator[elem])

# Метод .items()
for k, v in translator.items(): # -> (("cat", "кот"), ("dog", "пес"))
    print("Key:", k, "Val:", v)

