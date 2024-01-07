# Задача 19. Да се напише програма, която приема като вход текст и 
# обръща буквите от
# дясно наляво на само на думите, чиято дължина е нечетна, тези които
# са с четен брой си остават така като са.
# Вход: Bananas
# Изход: sananaB
# Вход: One two three four
# Изход: enO owt eerht four



senten = input('Write word or sentence: ')
sp = senten.split()
for i in sp:
    if len(i)%2 == 0:
        print(i)
    else:
        print(i[::-1], end=' ')