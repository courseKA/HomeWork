#Задача 3. Напишете програма, която намира най-голямото по стойност число, измежду три
#дадени числа.

x = int(input('Enter positive or negative digit: '))
y = int(input('Enter positive or negative digit: '))
z = int(input('Enter positive or negative digit: '))

if z > y and z > x:
    print('The biggest number is: ', z)
elif y > x and y > z:
    print('The biggest number is: ', y)
else:
    print('The biggest number is: ', x)
