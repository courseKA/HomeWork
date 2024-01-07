#Задача 7. Напишете програма, която прилага бонус точки към дадени точки в интервала [1..9]
#чрез прилагане на следните правила:
#- Ако точките са между 1 и 3, програмата ги умножава по 10.
#- Ако точките са между 4 и 6, ги умножава по 100.
#- Ако точките са между 7 и 9, ги умножава по 1000.
#- Ако точките са 0 или повече от 9, се отпечатва съобщение за грешка.

points = int(input('How many points do you have? (enter digit between 1 and 9): '))

if 3 >= points >= 1:
    print('Your bonus points are: ', points * 10)
elif 4 <= points <= 6:
    print('Your bonus points are: ', points * 100)
elif 7 <= points <= 9:
    print('Your bonus points are: ', points * 1000)
else:
    print('Error')