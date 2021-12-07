fruits = ["яблоко", "яблоко", "груша", "яблоко", "слива"]
fruit_count = {}  # создаём пустой ассоциативный массив
for fruit in fruits:
    # if not has_key(fruit_count, fruit):
    if fruit not in fruit_count:  # если в отображении нет такого ключа
        fruit_count[fruit] = 0   # заводим счётчик с таким ключом
    fruit_count[fruit] += 1    # увеличиваем счётчик:
# set(key, get(key) + 1)

print(fruit_count)

'''
class Map:

    pairs = []

    def get(key):
        for pair in pairs:
            if pair.key == key:  # пара с указанным ключом найдена
                return pair.value
        return None

    def set(key, value):
        for pair in pairs:
            if pair.key == key: # пара с указанным ключом найдена
                # обновить значение в найденной паре
                pair.value = value
                return
        # пара с заданным ключом не найдена
        добавить пару (key, value) в pairs
'''
