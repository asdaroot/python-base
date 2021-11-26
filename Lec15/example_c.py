# Супер-фокус
sample = (["a", "b", "c"],2,3,4)
sample[0][1] = "QQQQQQQQQ"
print(sample)


# Небольшое сравнение
nums_lst = [x for x in range(1, 100)]
nums_tuple =  tuple(nums_lst)
nums_set = set(nums_lst)

print("List:", nums_lst.__sizeof__(), "bytes")
print("Tuple:", nums_tuple.__sizeof__(), "bytes")
print("Set:", nums_set.__sizeof__(), "bytes")