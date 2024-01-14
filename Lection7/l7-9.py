'''Задача 9. Напишете програма, която създава следните квадратни матрици и ги
извежда на конзолата във форматиран вид. Размерът на матриците се въвежда от
конзолата. Пример за (4,4):'''
#a)
for i in range(1,5):
    for h in range(i, i + 13, 4):
        print(h, end=' ')
    print()
print('=' * 30)

for i,j,m,l in zip(range(1,6), range(5,10),range(9,14), range(13,17)):
 
    print(f'{i}\t{j}\t{m}\t{l}')
print('='*10,'end part a', '='*10)
#b)
list_numb = [1,8,9,13, 2,7,10,14, 3,6,11,15, 4,5,12,16]

# number of columns to be printed
numb_columns = 4
numb_rows = 4
# get length of list
len = len(list_numb)

# iterate over all row numbers
for i in range(numb_rows):
    # fetch content of each row, and print it
    sublist = list_numb[i*numb_columns : i*numb_columns + numb_columns]
 

    print(*sublist)   

