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


words = {
    0 : "first_word",
    1 : "second_word",
    2 : "third_word",
}

print(words[0], words[1], words[2])

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
# Ключ в словре - это любой элемент, который удовлетворяет слуд.условиям:
# 1) Этот элемент - представитель НЕИЗМЕНЯЕМОГО ТИПА!!!!
# 2) Ключ должны быть уникальными!