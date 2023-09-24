'''
Задача 8
Создайте пакет с всеми модулями, которые вы создали за время занятия.
Добавьте в __init__ пакета имена модулей внутри дандер __all__.
В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.
'''

from package_sem_6.module_task2_task3 import func
from package_sem_6.module_task4_5_6 import show_rezult, puzzle_solver, puzzle_solut
from package_sem_6.module_task_7 import calend

__all__ = ["func", "show_rezult", "puzzle_solver", "puzzle_solut", "calend"]