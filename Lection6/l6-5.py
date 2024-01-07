#Задача 5. Да се напише програма, която да намира броят на четните и нечетните числа
#от списък от цели числа.

numbs = [3,4,5,6,8,9,12,13,17]
ach = []
anch = []
for i in numbs:
    if i%2 == 0:
        ach.append(i)
    else:
        anch.append(i)
print('Sum of even numbers is: ',sum(ach))
print('Sum of odd numbers is :' ,sum(anch))