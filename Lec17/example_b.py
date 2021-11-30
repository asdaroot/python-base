def perimeter(side_a, side_b):
    result = 2 * (side_a + side_b)
    return result

# Объявляю явную функцию, которая
# будет просто ВЫВОДИТЬ в консоль слово Hello!
# И больше она ничего делать не будет!
def hello():
    print("Hello!")

hello() # Вызов явной функции hello()
# После того, как она отработает в консоли будет "Hello!"
print(perimeter(30, 40))
hello()