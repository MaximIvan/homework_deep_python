"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.
"""

# num = int(input())
# HEX_DIV = 16
# current_num = num
# res = ''
# num_16 = 'a', 'b', 'c', 'd', 'e', 'f'
# ost = 0

# while current_num > 0:
#     ost = current_num % HEX_DIV
#     if 10 <= ost <= 15:
#         match ost:
#             case 10:
#                 res += num_16[0]
#             case 11:
#                 res += num_16[1]
#             case 12:
#                 res += num_16[2]
#             case 13:
#                 res += num_16[3]
#             case 14:
#                 res += num_16[4]
#             case 15:
#                 res += num_16[5]      
#     else:
#         res += str(current_num % HEX_DIV)
#     current_num //= HEX_DIV

# res = res[::-1]

# print(res, hex(num))

# Вариант решения разобранный на семинаре:

TRANSLATE16 = {
    10: 'A', 11: 'B',
    12: 'C', 13: 'D',
    14: 'E', 15: 'F'
}

DIVIDER = 16

num= int(input('Введите число: '))
process16 = num
result16 = ''

while process16 > 0:
    result16 += TRANSLATE16.get(process16 % DIVIDER,
                                str(process16 % DIVIDER))
    process16 //= DIVIDER
result16 = result16[::-1]
print(f"""
Result: {result16}
Truth: {hex(num)}
""")