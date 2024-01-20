'''Задача 9. Напишете програма, която създава следните квадратни матрици и ги
извежда на конзолата във форматиран вид. Размерът на матриците се въвежда от
конзолата. Пример за (4,4):'''


for i,j,m,l in zip(range(1,6), range(8,4,-1),range(9,14), range(16,12, -1)):

    print(f'{i}\t{j}\t{m}\t{l}')

#second variant
for row in range(1,5):
    column = 1
    while column <= 4:
        if column % 2 != 0:
            col = row + 4*(column - 1)
        else:
            col = 4 * column - (row - 1)
        print(col, end=' ')
        column += 1
    print()