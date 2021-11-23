num_a = float(input())
num_b = float(input())
sign = input()


if sign == "/" and num_b == 0:
    print("СБОЙ") 
elif sign == "/" and num_b != 0:
    print(num_a / num_b) 
elif sign == "+":
    print(num_a + num_b) 
elif sign == "-":
    print(num_a - num_b)
elif sign == "*":
    print(num_a * num_b)
else:
    print("СБОЙ")
