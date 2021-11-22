## Лекция 12. Списки

* **Список** (list) - упорядоченная коллекция, способная хранить элементы любого типа.


### 1. Инициализация
* Пустой список можно создать при помощи :
```
a_list = []
b_list = list()

print("A_list:", len(a_list))
print("B_list:", len(b_list))
```

* Список с значениями:
```
numerics = [1, 2, 3, 5, 6, 7, 1, 2, -2]
print("Len:", len(numerics))
print("Numerics:", numerics)
```

* Список с значениями разных типов
```
numerics = [1, 2, 3, 5, 6, 7, 1, 2, -2, "Hello", "World", True, None]
print("Len:", len(numerics))
print("Numerics:", numerics)
```

### 2. Индексация и срезы списков
Идексация и срезы работают абсолютно также как и у строк!
```
words = ["a", "b", "c", "d"]
print("First:", words[0])
print("Last:", words[-1])

print("Slice:", words[0:3:1])
```

### 3. Длина и вхождение
* Длина списка
```
print("Len:", len(words))
```

* Проверка вхождения
```
if "c" in words: # Проверка вхождения ЭЛЕМЕНТА "c" в список ["a", "b", "c", "d"]
    print("c in words")
else:
    print("c not in words")
```


### 4. Итеририрование
* Перебор элементов списка по индексу
```
for i in range(len(words)):
    print(f"id: {i}, elem: {words[i]}")
```

* Итерирование через элементы
```
for elem in words:
    print("Elem:", elem)
```

### 5. Сумма, минимум и максимум
* Для подсчета суммы - все элементы должны быть числовыми или приводимыми к числовому типу.

* Для поиска мин/макс - необходимо , чтобы все элементы были сравинимы между собой

```
nums = [10, 20, 30, 40, 50]
print("Sum:", sum(nums))


print("Min:", min(nums))
print("Max:", max(nums))
```

### 5.1 Сравнение строк
* Команда `ord(symbol:str)` - возвращает код символа.
```
# ord() 
print("Ord of 'a' is:", ord("a"))
print("Ord of 'b' is:", ord("b"))
print("Ord of 'A' is:", ord("A"))
print("Ord of 'B' is:", ord("B"))
```

* Комада `chr(code:int)` - возвращает символ по коду

* В `Python 3.x` - все хранится в `unicode`

* Простой пример сравнения
```
print("a" > "A") # 97 > 65
```
* 
Пример сравнения слов из двух букв
```
print("abc" > "a")
# Сначала пытаются сравниться первые символы. Если они равны (равны их коды),
# то сравниваются вторые символы между собой и так далее, до тех пор, пока
# между двумя символами нельзя будет поставить знак > или <
```

### 6. Добавление/удаление
* Добавление в конец :
```
nums = []
nums.append(10) # Добавляет значение в конец списка
nums.append(20) 
```

* Добавление в середину:
```
nums = [10, 20, 30, 40]
nums.insert(10, 99999) # При вставке в несуществующий индекс - элемент будет добавлен в конец списка!
print("Nums:", nums)
```

* Удалeние из конца (первого с конца)
```
elem = nums.pop()
print("Elem after pop:", elem)
print("Nums after pop:", nums)
```

* Удаление по значению (первого попавшегося элемента)
```
if 30 in nums:
    nums.remove(30)

print("Nums agter remove:", nums)
```

### 7. Изменяемость и ссылочность
* Список - изменяемая коллекция
```
nums = [10, 20, 30 , 40]
nums[0] = 9999999999

print(nums)
```

* Ссылочность:
```
# Ссылочность списков
a_list = [1, 2, 3] # oxfxofx8ff39191
b_list = a_list[:] # a_list.copy()

b_list.append("Vasya")

print("A_list:", a_list)
print("B_list:", b_list)
```