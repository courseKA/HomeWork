'''Задача 4. Да се създаде програма, която да чете цели числа въведени от потребителя,
докато не бъде въведен празен ред. След като всичките числа са прочетени, програмата
трябва да показва всички отрицателни числа, последвани от нули, последвани от всички
положителни числа. Във всяка група номерата трябва да се показват в същия ред, в
който са въведени от потребителя. Например, ако потребителят въведе стойностите 3, -
4, 1, 0, -1, 0 и -2, вашата програма трябва да изведе стойностите -4, -1, -2, 0, 0, 3 и 1 .
Вашата програма трябва да показва всяка стойност на нов ред.'''
#define how many numbers in list
n = int(input('Please insert number of numbers: '))
#create empty lists
lst_negative = []
lst_zero = []
lst_pozitive = []

for user_input in range(n):
    user_input = int(input('Please enter a number: '))
    #if user input is digit add to list
    if user_input >0:
        lst_pozitive.append(user_input)
        continue
    elif (user_input) <0:
        lst_negative.append(user_input)
        continue
    elif (user_input) == 0:
        lst_zero.append(user_input)
        continue
    else:
        print('Please enter a real number integer: ')
print(*(lst_negative + lst_zero + lst_pozitive), sep=',')



