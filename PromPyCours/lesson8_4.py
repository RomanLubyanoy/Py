# -*- coding:utf-8 -*-
"""
Розробити функцію make_sudoku(size),
яка приймає 1 аргумент -- додатнє ціле число (1 <= size <= 42),
та повертає список списків -- квадратну матрицю, що представляє
судоку розмірності size.

Судоку розмірності X являє собою квадратну матрицю розмірністю X**2 на X**2,
розбиту на X**2 квадратів розмірністю X на X, заповнену цілими числами таким чином,
щоб кожна вертикаль, кожна горизонталь та кожний квадрат містили всі числа
від 1 до X**2 включно без повторів.

-- квадрат 9х9 (3**2 = 9), який складається з 9 квадратів 3х3.
В кожній вертикалі розміщені різні числа від 1 до 9.
Те саме стосується кожної горизонталі та кожного внутрішнього квадрату.

Дане завдання не має єдиного вірного розв'язку -- ваша функція повинна
повертати результат, який задовольняє умові, за відведений час.

Тести із некоректними даними не проводяться

Приклад вхідних і вихідних даних:
print make_sudoku(1) # [[1]]
print make_sudoku(2) # [[1,2,3,4],
                        [3,4,1,2],
                        [2,1,4,3],
                        [4,3,2,1]]
print make_sudoku(3) # [[3,5,8,1,2,7,6,4,9],
                        [6,7,4,5,8,9,3,2,1],
                        [2,1,9,3,4,6,5,7,8],
                        [9,8,6,7,1,4,2,5,3],
                        [4,3,1,2,6,5,8,9,7],
                        [7,2,5,9,3,8,1,6,4],
                        [1,6,3,4,7,2,9,8,5],
                        [8,9,7,6,5,1,4,3,2],
                        [5,4,2,8,9,3,7,1,6]]
"""
from random import shuffle


def make_sudoku(size):
    vals = [i for i in range(1, size ** 2 + 1)]
    rez = [[0 for j in range(1, size ** 2 + 1)] for i in range(1, size ** 2 + 1)]
    shuffle(vals)
    r_value = vals[::]
    c_value = vals[1:]
    shuffle(c_value)
    r_count = 0
    c_count = 1

    for s_size in range(len(rez)):

        for ii in range(0, len(r_value)):
            rez[r_count][s_size] = r_value[ii]
        for jj in range(0, len(c_value)):
                rez[jj + 1][c_count - 1] = c_value[jj]
#        print r_value
#        print c_value

        r_value.pop()
        r_count += 1

    return rez
"""
    while count != 1:
        rez = []
        for i in range(size ** 2):
            shuffle(vals)
            rez.append(vals[::])
        count = 0
        for ii in range(size ** 2):
            sud = set()
            for jj in range(size ** 2):
    #            print rez[jj][ii]
                sud.add(rez[jj][ii])
#            print len(sud)
            if len(sud) == size ** 2:
                count += 1
            else:
                break
    return rez
"""
l = make_sudoku(3) # [[1]]
#print l
print '----------'
for ii in range(len(l)):
    print l[ii]
#print set(l[0][0], l[1][0], l[2][0], l[3][0])


"""
l = [1, 2, 3, 4]
shuffle(l)
print l
shuffle(l)
print l
shuffle(l)
print l
"""