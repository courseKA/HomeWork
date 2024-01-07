#Задача 14. Сортирайте 3 реални числа в намаляващ ред. Използвайте вложени if оператори.

a = int(input('Enter numb: '))
b = int(input('Enter numb: '))
c = int(input('Enter numb: '))


if a > b and b > c:
    print(a, b, c)
elif a > c and c > b:
    print(a, c, b)
elif b > a and a > c:
    print(b, a, c)
elif c > a and b > c:
    print(b, c, a)
elif c > a and a > b:
    print(c, a, b)
else:
    print(c, b, a)