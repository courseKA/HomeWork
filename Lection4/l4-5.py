#Задача 5. Напишете програма, която при въвеждане на коефициентите (a, b и c) на квадратно
#уравнение ax^2+bx+c изчислява и извежда неговите реални корени.

import math
# in order to have 2 roots discriminant has to be > 0 - b**2 - 4ac > 0

a = int(input('Enter positive or negative digit: '))
b = int(input('Enter positive or negative digit: '))
c = int(input('Enter positive or negative digit: '))
x1 = 0
x2 = 0
y1 = int(b**2 - 4 * a * c)

bot = 2 * a
if y1 > 0:
    x1 = (-b + math.sqrt(y1))/bot
    print(x1)
    x2 = (-b - math.sqrt(y1))/(bot)
    print(x2)
elif y1 < 0:
    print('No real roots')
else:
    print( x1 == x2 == -b/bot)
