"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.
"""

num = int(input())
HEX_DIV = 16
current_num = num
res = ''
num_16 = 'a', 'b', 'c', 'd', 'e', 'f'
ost = 0

while current_num > 0:
    ost = current_num % HEX_DIV
    if 10 <= ost <= 15:
        match ost:
            case 10:
                res += num_16[0]
            case 11:
                res += num_16[1]
            case 12:
                res += num_16[2]
            case 13:
                res += num_16[3]
            case 14:
                res += num_16[4]
            case 15:
                res += num_16[5]      
    else:
        res += str(current_num % HEX_DIV)
    current_num //= HEX_DIV

res = res[::-1]

print(res, hex(num))