# Задача B. Очередь

n = int(input().strip())
events = [] # Список событий
for _ in range(n):
    events.append(input().strip())

queue = [] # Моя очередь - тут будут только фамилии
for event in events:
    if "Следующий" in event:
        if len(queue) > 0 :
            person = queue.pop(0) # По умолчанию удаляет последний!
                                  # если передан индекс - то выкинет элемент с индексом
            print(f"Заходит {person}!")
        else:
            print("В очереди никого нет.")
    elif "Кто последний?" in event:
        temp_lst = event.split(" - ") # ["Кто последний? Я", "Кузнецов."]
        queue.append(temp_lst[-1].split(".")[0]) # ["Кузнецов", ""][0]
    elif "Я только спросить" in event:
        temp_lst = event.split(" - ") # ["Я только спросить! Я", "Иванова."]
        queue.insert(0, temp_lst[-1].split(".")[0]) # ["Иванова", ""][0]
