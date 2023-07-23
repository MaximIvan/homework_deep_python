"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]
"""

my_list = [1, 2, 3, 1, 2, 4, 5]

my_set = set()

for num in my_list:
    if my_list.count(num) > 1:
        my_set.add(num)

print(my_list)
print(list(my_set))

