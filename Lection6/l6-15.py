# Задача 15. Да се напише програма, която подканва потребителя да въведе число и
# програмата да провери дали то е просто или не.
# Вход:
# Please enter a number
# >>> 12
# Изход:
# The number is not prime.

a = int(input('Write number less than 50: '))

for i in range(2,a):
    if a%i ==0:
        print('number is not prime')
        break
    else: 
        print('number is prime')
        break