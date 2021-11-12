# Задача F. Уравнение

"""
ax^2 + bx + c = 0
На вход программе идут a,b,c
Нужно сказать - сколько корней имеет уравнение с
данными коэффициентами?

Гарантируется, что как минимум ОДИН КОЭФФИЦИЕНТ не равен 0


D = b^2 - 4ac
Если D > 0 - КОРНЯ 2
Если D == 0 - Корень 1
ЕСЛИ D < 0 - Нет корней

Если a == 0:
    bx + c = 0
    Если b != 0 
    x = - c/b
    Если b == 0
    Решений нет (нет корней)
Иначе:
    Считаем дескриминант и по знаку определяем количество корней
"""