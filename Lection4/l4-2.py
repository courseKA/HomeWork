#Задача 2. Напишете програма, която показва знака (+ или -) от частното на две реални числа,
#без да го пресмята.

a = int(input('Enter positive or negative digit: '))
b = int(input('Enter positive or negative digit: '))

if a > 0 and b > 0:
    print('+')
elif a > 0 and b < 0:
    print('-')
elif a < 0 and b > 0:
    print('-')
else:
    print('+')
