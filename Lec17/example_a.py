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

# if perimeter(10, 20) is not None:
#     pass







# y(1) = 1^2 + 4*1 + 3
# y(2) = 2^2 + 4*2 + 3