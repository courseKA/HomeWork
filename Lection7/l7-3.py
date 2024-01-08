'''Задача 3. Да се създаде програма, която чете думи като вход от клавиатурата, докато
потребителят не въведе празен ред. След като потребителят въведе празен ред,
програмата трябва да изведе всяка дума, въведена от потребителя точно веднъж.
Думите трябва да се показват в същия ред, в който са били въведени. Например, ако
потребителят въведе:
first
second
first
third
second
тогава програмата трябва да принтира само:
first
second
third'''

words = []
while True:
    word = str(input('Please write word: '))
    if word.isdiit() == True:
        print('Please write word not digit')
    elif not word:
        for word in words:
            print(word)
        exit()
    elif word not in words:
        words.append(word)
    elif word in words:
        continue
    else:
        break

