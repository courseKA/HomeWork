#7. . Високосни години са всички години кратни на 4 с изключения столетията, но без столетия кратни на 400, т.е. 1900 не е високосна,
#но 1600 и 2000 са високосни. Съставете програма, която по въведен ден, месец, година отпечатва следващата дата.
#Входни данни: естествени числа за ден, месец, година.


month_31 = 1,3,5,7,8,10,12
month_30 = 4,6,9,11
month_2 = 2

year = int(input('year : '))
month = int(input('month: '))
day = int(input('day: '))

if month in month_31 and day <= 30:
    print((day + 1), month, year, sep=',')
elif month in month_31 and day == 31:
    print('1', (month + 1), year, sep=',')
elif month in month_30 and day <= 29:
    print((day + 1), month, year, sep=',')
elif month in month_30 and day == 30:
    print('1', (month + 1), year, sep=',')
elif month == month_2 and day <= 27:
    print((day + 1), month, year, sep=',')
elif month == month_2 and day == 28 and year%4 != 0 and year%400 == 0:
    print('1', (month + 1), year, sep=',')
elif day == 28 and month == month_2 and year%4 == 0 and year%400 != 0:
    print((day + 1), month, year, sep=',')
else:
    print('Enter correct number: ')





