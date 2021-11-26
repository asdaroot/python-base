# Считываем набор цифр и считаем его сумму
input_nums = "1 2 3 4 5 6 7 8 9 10"
input_list_str = input_nums.split() # ["1", "2", "3", "4", "5",..]
input_list_int = []


for elem in input_list_str:
    input_list_int.append(int(elem))

print("Sum:", sum(input_list_int))

