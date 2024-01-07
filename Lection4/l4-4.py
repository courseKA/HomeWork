#Задача 4. Напишете програма, която за дадена цифра (0-9), зададена като вход, извежда името
#на цифрата на български език.
a = int(input('Insert digit from 0 to 9: '))

if a == 0:
    print('Нула')
elif a == 1:
    print('Едно')
elif a == 2:
    print('Две')
elif a == 3:
    print('Три')
elif a == 4:
    print('Четири')
elif a == 5:
    print('Пет')
elif a == 6:
    print('Шест')
elif a == 7:
    print('Седем')
elif a == 8:
    print('Осем')
else:
    print('Девет')
        