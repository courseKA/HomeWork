'''Задача 5. За да спечели най-голямата награда в определена лотария, човек трябва да
съпостави всичките 6 числа от билета си с 6-те числа между 1 и 49, които са изтеглени от
организатора на лотарията. Напишете програма, която генерира произволен избор от 6
числа за лотариен билет. Уверете се, че избраните 6 числа не се повтарят. Покажете
числата във възходящ ред.'''

import random

#create a list lottery numbers
lottery_numbers = [3,8,22,33,45,49]
#create empty list
numbers = []
#create list of 6 random numbers
for i in range (6):
    numb = random.randint(1,49)
    #if the number repeats, generate new number
    if numb in numbers:
        numb=random.randint(1,49)
    numbers.append(numb)
print(*numbers)
#find weather guessed
duplicates = set(lottery_numbers) & set(numbers)
print('You guessed: ', duplicates)
