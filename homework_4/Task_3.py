'''
3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''

from datetime import date, datetime


COMM_WITHDRAWAL = 1.5
COMM_REFIL = 3
TAX = 10
COMM_MIN = 30
COMM_MAX = 600
SUM_WORK = 50
MAX_COUNT = 5_000_000
account = 0
count_refil = 0
count_withdrawal = 0

def get_money(input_string:str)->int:
    while True:
        try:
            num = int(input(input_string))
            if num > 0 and num % SUM_WORK == 0:
                return num
            else:
                print('Сумма должна быть положительной и кратной 50')
        except ValueError:
            print('Это не то...')

def refil_account(num:int):
    global account 
    account += num

def account_proc():
    num = account/100*COMM_REFIL
    refil_account(num)

def take_account(num:list):
    global account 
    account -= num

def take_tax():
    if account > MAX_COUNT:
        num = account/100*TAX
        take_account(num)

def chek_money(num):
    proc = num/100*COMM_WITHDRAWAL
    if proc < COMM_MIN:
        num += COMM_MIN
    elif proc > COMM_MAX:
        num += COMM_MAX
    else:
        num += proc
    return num


result_operation = []

print('Здравствуйте. Это программа банкомат\n')
while True:
    choice = int(input('Выберите действие:\n'
        '1 - пополнить счет\n'\
        '2 - снять деньги со счета\n'
        '3 - посмотреть историю операций\n'
        '4 - выход\n'))
    match choice:
        case 1:
            number = get_money('Введите сумму для зачисления на счет:\n')
            take_tax()
            refil_account(number)
            count_refil += 1
            if count_refil == 3:
                account_proc()
                count_refil = 0
            print(f'У вас на счету: {account} рублей')

            result_operation.append([str(datetime.today()), + 1 * number])
            result_operation.append([str(datetime.today()), account])

        case 2:
            number = get_money('Введите сумму для снятия со счета:\n')
            take_tax()
            number = chek_money(number)
            if number < account:
                take_account(number)
                count_withdrawal += 1
                if count_withdrawal == 3:
                    account_proc()
                    count_withdrawal = 0

                result_operation.append([str(datetime.today()), -1 * number])
                result_operation.append([str(datetime.today()), account])
            else:
                print('Недостаточно средств')
            print(f'У вас на счету: {account} рублей')
        
        case 3:
            print(f'{result_operation}\n')
        
        case 4:
            print('До свидания')
            print(f'У вас на счету: {account} рублей')
            break
        
        case _:
            print('Не известная команда')