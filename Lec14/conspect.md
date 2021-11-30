## Лекция 14. Str-To-List методы

### 1. Строковый метод .split()
* При помощи метода `.split(sep)` можно превращать входную строку в список элементов строки, который получится в результате разделения исходной строки по некому `sep` - разделителю.

```
# Считываем набор цифр и считаем его сумму
input_nums = "1 2 3 4 5 6 7 8 9 10"
input_list = input_nums.split(sep=" ") # ["1", "2", "3", "4", "5",..]

print(input_list)
```

* `sep` - разделитель - не может быть пустой строкой `""`.
* `sep` - только строка
* если `sep` не встречается в исходнике - на выходе список с одной строкой!
* `sep` - всегда одна фраза! Группу `sep` опеределить нельзя (т.е. не возможно использовать например список `sep`в одном `.split()`)
* `sep` по умолчанию равен символам "пустоты" (`\n`, `\t`, ` `)


* Пример задачи на считывание набора цифр (в одну строку) и преобразования к `int` для подсчета суммы.
```
# Считываем набор цифр и считаем его сумму
input_nums = "1 2 3 4 5 6 7 8 9 10"
input_list_str = input_nums.split() # ["1", "2", "3", "4", "5",..]
input_list_int = []


for elem in input_list_str:
    input_list_int.append(int(elem))

print("Sum:", sum(input_list_int))
```

### 2. Строковый метод .join()
* `sep.join(lst[str])` - в результате вернет строку, состоящую из элементов списка `lst` разделенных между собой `sep` (`lst[0]+set+lst[1] + sep + lst[2] + sep + ..)`
* `sep` - это строка!
* `lst[str]` - список строк!

* Пример использования `join`
```
# Пример `.join()`

words = ["aaa", "bbb", "ccc"]
message = "-@-".join(words)
print(message)
```

* Пример использования `join` в задаче конкатенации целых чисел:
```
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(nums)):
    nums[i] = str(nums[i])

output = " ".join(nums)
print(output)
```

### 3. Списочные выражение и методы split/join
* Решение задачи с методом `split`:
```
print("Sum:", sum([int(letter) for letter in "1 2 3 4 5 6 7 8 9 10".split()]))
```

* Решение задачи с методом `join`:
```
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(", ".join([str(elem) for elem in nums]))
```