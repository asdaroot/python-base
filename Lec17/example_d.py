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