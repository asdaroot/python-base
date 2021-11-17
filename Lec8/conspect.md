## Лекция 8. Цикл for

### 1. Синтаксис
```
for expression:
    body
```

### 2. Отличие от while
* `while` - можно запускать в виде условно-бесконечного цикла
* `for` - оптимизированный цикл (работает быстрее `while`), но финитный

### 3. Пример
```
# While
i = 0

while i < 10:
    print("Current:", i)
    i += 1

# For
for i in range(0, 10, 1):
    print("Current:", i)
```


### 4. range()
* `range` - диапазон (итератор), позволяющий изменять значения переменных по указанным правилам диапазона.