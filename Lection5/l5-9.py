#9. Да се състави програма, която да провери дали е възможно един
#правоъгълник да се вмести изцяло в друг правоъгълник.
#Входни данни: X1, Y1, X2, Y2 - страните на 2-та правоъгълника - естествени числа от
#интервала [5 ..100].
#Пример: 5, 12; 18,7 Изход: вместват се

#first
a = int(input('Insert digit between 5 and 100: '))
b = int(input('Insert digit between 5 and 100: '))

#second
c = int(input('Insert digit between 5 and 100: '))
d = int(input('Insert digit between 5 and 100: '))

if a < c and b < d and b < c and a < d:
    print('Първият правоъгълник се вмества във втория.')
elif c < a and d < b and d < a and c < b:
    print('Вторият правоъгълник се вмества в първия.')
else: 
    print('Триъгълниците не се вмесват един в друг')