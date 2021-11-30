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