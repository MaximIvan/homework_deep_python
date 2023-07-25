"""
8. ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

item_dict = {'Вася': {'рюкзак', 'палатка', 'котелок', 'фонарик'},
             'Коля': {'рюкзак', 'палатка', 'фонарик', 'спички'},
             'Миша': {'рюкзак', 'палатка', 'спички', 'велосипед'}}

res1 = set()

for i in item_dict:
    if not res1:
        res1 = set(item_dict[i])
    else:
        res1 &= set(item_dict[i])

print('Список вещей, которые взяли все друзья:', res1)

my_tuple = item_dict.keys()

my_set = set()
for friend in my_tuple:
    my_set = set(item_dict[friend])

    for other_friends in [i for i in my_tuple if i != friend]:
        my_set = my_set - set(item_dict[other_friends])
    
    if my_set:
        print('Какие вещи уникальны, есть только у одного друга:', my_set)

for friend in my_tuple:
    to_remove = set(item_dict[friend])
    my_set = set()
    for other_friends in [i for i in my_tuple if i != friend]:
        if not my_set:
            my_set = set(item_dict[other_friends])
        else:
           my_set = my_set & set(item_dict[other_friends])

    my_set -= to_remove
    
    if my_set:
        print(f'Вещи есть у всех друзей кроме одного: {friend} не взял {my_set}')