# Перезапись задачи example_a.py
# Считываем набор цифр и считаем его сумму
# input_nums = "1 2 3 4 5 6 7 8 9 10"
# input_list_str = input_nums.split() # ["1", "2", "3", "4", "5",..]
# input_list_int = []


# for elem in input_list_str:
#     input_list_int.append(int(elem))

# print("Sum:", sum(input_list_int))

input_nums = "1 2 3 4 5 6 7 8 9 10"
input_nums_str = input_nums.split() # ["1", "2", "3", "4", "5",..]
input_nums_ints = [int(letter) for letter in input_nums_str]

print("Sum:", sum(input_nums_ints))


## Делаем короче
input_nums_str = "1 2 3 4 5 6 7 8 9 10".split() # ["1", "2", "3", "4", "5",..]
input_nums_ints = [int(letter) for letter in input_nums_str]

print("Sum:", sum(input_nums_ints))

# Делаем еще короче
input_nums_ints = [int(letter) for letter in "1 2 3 4 5 6 7 8 9 10".split()]
print("Sum:", sum(input_nums_ints))

# ЕЩЕ КОРОЧЕ!
print("Sum:", sum([int(letter) for letter in "1 2 3 4 5 6 7 8 9 10".split()]))