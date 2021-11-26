# Задача - перевести список строк в список интов за 1 строчку!
data = ["1", "2", "3"]

lst = [int(letter) for letter in data] # ["0", "1", "2", "3", "4", ...]
print(lst)


data_ints = [1, 2, 3, 4, 5, 6, 7, 8]
print([str(num) for num in data_ints])