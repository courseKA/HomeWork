'''Задача 6. Да се напише програма, която генерира всички подсписъци на даден списък.
Например, списъците на [1, 2, 3] са [], [1], [2], [3], [1, 2], [2, 3], [1, 3] и [1, 2, 3].'''

lst = [1,2,3]
l_new = [[]]
for i in lst:
    l_new += [x +  [i] for x in l_new]

print(*(l_new))