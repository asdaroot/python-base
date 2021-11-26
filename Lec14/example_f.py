# Перепишем задачу с join()
# Вариант с join()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(nums)):
    nums[i] = str(nums[i])

output = ", ".join(nums)
print(output)

# Делаем короче
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_str = [str(elem) for elem in nums]
output = ", ".join(nums_str)
print(output)

# Делаем еще короче
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(", ".join([str(elem) for elem in nums]))