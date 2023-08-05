'''
Расчет общей стоимости портфеля акций: Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float принимает два аргумента: stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.), и значениями - количество акций каждого символа. prices - словарь, где ключами являются символы акций, а значениями - текущая цена каждой акции. Функция должна вернуть общую стоимость портфеля акций на основе количества акций и их текущих цен.
'''

def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    global _res
    _res = []
    for elem in zip(stocks.values(), prices.values()):
        _res.append(elem[0]*elem[1])
    total = sum(_res)
    print(total)
    

'''
Расчет доходности портфеля: Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float принимает два аргумента: initial_value - начальная стоимость портфеля акций. current_value - текущая стоимость портфеля акций. Функция должна вернуть процентную доходность портфеля.
'''


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    difference_income = current_value - initial_value
    procent_income = round((difference_income/initial_value)*100, 2)
    print(f'Процентная доходность портфеля составляет: {procent_income}%')



'''
Определение наиболее прибыльной акции: Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str принимает два аргумента: stocks - словарь с акциями и их количеством. prices - словарь с акциями и их текущими ценами. Функция должна вернуть символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью. Начальная стоимость - первый вызов calculate_portfolio_value, данные из этого вызова следует сохранить в защищенную переменную на уровне модуля.
'''


def get_most_profitable_stock(stocks: dict, current_prices: dict) -> str:
    current_res = []
    for elem in zip(stocks.values(), current_prices.values()):
        current_res.append(elem[0]*elem[1])
  
    different_res = {}
    for stock, num, current_num in zip(stocks, _res, current_res):
        different = current_num - num
        different_res[stock] = different

    print(max(different_res, key=different_res.get))
