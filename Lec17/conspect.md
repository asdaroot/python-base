## Лекция 17. Функции. Начало

Функции - блок кода, к которому можно обращаться при необходимости.
Функции бывают:
* явные (у которых есть имя)
* неявные (анонимные) (у которых нет имени)

### 1. Явные функции
* Явная функция - это функция определнная через `def` и имеющая ЯВНОЕ ИМЯ!
```
# y(x) = x^2 + 4x + 3 - объявление явной функции
# у нее есть имя - y
# у нее есть входные парметры - x
# у нее есть тело - x^2 + 4x + 3

# Подсчет периметра - объявление явной функции
def perimeter(side_a, side_b):
    result = 2 * (side_a + side_b)
    return result
# у нее есть имя - perimeter
# у нее есть входные парметры - side_a, side_b
# у нее есть тело - result = 2 * (side_a + side_b)


BASE_A, BASE_B = 10, 10
# ВЫЗОВ явной функции perimeter(10, 10) -> 40
per = perimeter(BASE_A, BASE_B) # 40
print(per)
```
 
### 2. Явные функции без входных параметров
```
def hello():
    print("Hello!")

hello() # Вызов!
```

### 3. Явные функции - возврат значений
```
def perimeter(side_a, side_b):
    result = 2 * (side_a + side_b)
    print(result)
    #return result # Вернуть на место вызова функции это значение
    #return None

def hello():
    print("Hello!")
    #return None - если явно не указан return - любая функция в Python
                # по умолчанию возвращает None

per = perimeter(10, 20)
print("per value:", per)
res = hello()
print(res)
```

* Возврат None:
```
# Любой код ниже слова return игнорируется,
# потому что в момент вызова return управление передается вызывающей стороне и код
# ниже не отрабатывает
def shaper(side_a, side_b):
    print("Shape a:", side_a)
    return # Пустой return == return None
    print("Shape b:", side_b)
    
    area = side_a * side_b
    return area

res = shaper(10, 20) # 200
print(res)
```