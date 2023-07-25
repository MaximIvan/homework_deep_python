"""
3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. 
*Верните все возможные варианты комплектации рюкзака.
"""

from operator import itemgetter

list_things = {'котелок': 1, 'палатка': 7, 'топор': 3, 'фляга': 2, 'плащ': 1, 'рыболовные снасти': 6, 'велосипед': 14}
max_capacity_backpack = 15
weight = 0
capacity_backpack = 0

print('список вещей: ', list_things)
print('максимальная грузоподьемность рюкзака', max_capacity_backpack, 'кг')

for thing, capacity in dict(sorted(list_things.items(), key=itemgetter(1))).items():
    weight += list_things[thing]
    if weight <= max_capacity_backpack:
        print(thing, '=', capacity)
        capacity_backpack += list_things[thing]

print(f'Вес рюкзака c вещами: {capacity_backpack} кг')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Все возможные вариант заполнения рюкзака:')
list_dict_value = []
list_dict_key = []
for key, value in list_things.items():
    list_dict_key.append(key)
    list_dict_value.append(value)

def subset_sum(weights, things, target, count, partial_weights=[], partial_things=[]):
    s = sum(partial_weights)

    if s <= target:
        print("список вещей(%s)\nвес вещей(%s) <= %s \n" % (partial_things, partial_weights, target))

    if s >= target:
        return  

    for i in range(len(weights)):
        n = weights[i]
        remaining_weights = weights[i + 1:]
        m = things[i]
        remaining_things = things[i + 1:]
        subset_sum(remaining_weights, remaining_things, target, count + 1, partial_weights + [n], partial_things + [m])

print(subset_sum(list_dict_value, list_dict_key, max_capacity_backpack, 0))