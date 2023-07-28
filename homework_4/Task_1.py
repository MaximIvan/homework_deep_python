'''
1. Напишите функцию для транспонирования матрицы. 
Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
'''

matrix = [[1, 2, 3], 
          [4, 5, 6]]


def change_matrix(matrix):
    new_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    print(new_matrix)


print('Исходная матрица:')
print(matrix)
print('транспонированная матрица:')
change_matrix(matrix)
