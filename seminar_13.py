'''
1. Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число. 
Обрабатывайте не числовые данные как исключения.
'''


# def correct_input():
#     while True:
#         try:
#             num = float(input('Введите число:'))
#             break
#         except ValueError as e:
#             print(f'Вы ввели не число. Ошибка: {e}')
#     return num

# if __name__ == '__main__':
#     print(correct_input())


'''
2. Создайте функцию аналог get для словаря. 
Помимо самого словаря функция принимает ключ и значение по умолчанию. 
При обращении к несуществующему ключу функция должна возвращать дефолтное значение. 
Реализуйте работу через обработку исключений.
'''


# class MyDict(dict):

#     def my_get(self, key_, value_ = None):
#         try:
#             return self[key_]
#         except KeyError:
#             return value_

# if __name__ == '__main__':
#     mg = MyDict({'one': 1, 'two': 2})
#     print(mg)
#     print(mg['one', 'john'])
#     print(mg)
#     print(mg['sdf'])


'''
3. Создайте класс с базовым исключением и дочерние 
классы-исключения: ошибка уровня, ошибка доступа.
'''


import json


class MyException(Exception):
    pass


class MyExceptionLevel(MyException):
    pass


class MyExceptionAccess(MyException):
    pass

'''
4.
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
'''


class User:
    def __init__(self, user_id: int, level: int, user_name: str) -> None:
        self.level = level
        self.__user_id = user_id
        self.user_name = user_name

    def load(self, file_name: str):
        with open(f'{file_name}.json', 'r', encoding='utf-8') as file_json:
            data = json.load(file_json)
        #    print(data)
        users: set = set()
        for one_user in data:
            print(*one_user.values())
            users.add(User(*one_user.values()))
        return users

    def __eq__(self, other):
        return self.user_name == other.user_name and self.__user_id == other.__user_id
    
    def __hash__(self):
        return int(self.__user_id)

    def __repr__(self):
        return f'Имя: {self.user_name} Id: {self.__user_id} Уровень доступа: {self.level} '
    
if __name__ == '__main__':
    p1 = User(user_id=7, level=7, user_name="Test")
    print(p1.load(file_name='test'))


'''
5. Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. 
Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей. 
Если такого пользователя нет, вызывайте исключение доступа. 
А если пользователь есть, получите его уровень из множества пользователей.
добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
'''


class Project:
    def __init__(self):
        self.users = User(level = 7, user_id = 132340, user_name = "Alex").load("test")
        self.entered_user = None

    def reload_users(self):
        self.users = User(level = 7, user_id = 132340, user_name = "Alex").load("test")

    def enter(self, id: int, name: str):
        that_user = User(level = None, user_id = id, user_name = name)
        if that_user not in self.users:
            raise MyExceptionAccess
        for i in self.users:
            if i == that_user:
                self.entered_user = i

    def add_user(self, id, level, name):
        if self.entered_user.level < level:
            raise MyExceptionLevel
        self.users.add(User(id, level, name))

if __name__ =="__main__":
    proj = Project()
    proj.enter("000021", "Fedor")
    proj.add_user("093943", 2, "Anna")
    print(proj.users)