#Задача 12. Напишете програма, която да използва следните променливи, възраст – age, пол
#(M или F), семейно положение (Y или N) за даден служител. Според следните правила,
#програмата да определя, къде може да работи конкретният служител.
#Правила:
#- Ако служителката е жена, тя може да работи само в градски райони.
#- Ако служителят е мъж на възраст между 20 до 40 години, той може да работи навсякъде
#- Ако служителят е мъж на възраст между 40 и 60 години, той ще работи само в градските
#райони
#За всяка друга възраст трябва да се отпечатва грешка

age = int(input('Insert your age: '))
gender = input('If you are man write M or woman write W: ')
status = input('If you are married write Y or if no write N: ')

if gender == 'W':
    print('You can work only in the city.')
elif gender == 'M' and age > 24 and age < 40:
    print('You can work everywere.')
elif gender == 'M' and age > 40 and age < 60:
    print('You can work only in the city.')
else:
    print('Error')