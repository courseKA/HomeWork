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
#create empty list
words = []
#with while loop execute a set of statement
while True:
    word = str(input('Please write word: '))
    #check wheather word is string
    if word.isdiit() == True:
        print('Please write word not digit')
    #check wheather word input is empty
    elif not word:
    #if is empty print all words and exit
        for word in words:
            print(word)
        exit()
    #if word is not in list add word to words
    elif word not in words:
        words.append(word)
    #if word is in words continue without to add word
    elif word in words:
        continue
    else:
        break

