# Есть список чисел - надо получить одну строку состоящую из этих чисел,
# разделенных пробелом

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

output_str = ""
for elem in nums:
    output_str += str(elem) + " "

print(output_str)