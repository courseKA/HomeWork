#3. Трябва да се напълни цистерна с вода. Имате 2 кофи с вместимост 2 и 3 литра и ги ползвате едновременно. 
#Да се състави програма, която по въведен обем извежда как ще прелеете течността с тези кофи, т.е. 
#по-колко пъти ще се пълни всяка от кофите.
#Входни данни: естествено число от интервала [10..9999].

#Enter valid value:
while True:
    try:
        obem = int(input('Write digit between 10 and 9999: '))
        if 10<=obem<=9999:
            break
        else:
            print('Interval must be: [10-9999]')
    except:
        print('Enter correct digit')
        
obem = int(input('Write digit between 10 and 9999: '))
k1 = 2
k2 = 3
obem_kofi = k1 + k2
ob_broi = obem//obem_kofi
ostatak = obem%5
    
if obem%5 != 0 and ostatak%2 == 0 and ostatak//2 == 1:
    print('Each bucket will be full ', ob_broi, 'times and additional one bucket', k1)
elif obem%5 != 0 and ostatak%2 == 0 and ostatak//2 == 2:
    print('Each bucket will be full ', ob_broi, 'times and additional two buckets 2 l - ', 2*k1, 'liters')
elif obem%5 != 0 and ostatak%3 == 0 and ostatak//3 == 1:
    print('Each bucket will be full ', ob_broi, 'times and additional one bucket', k2)
elif obem%5 == 0:
    print('Each bucket will be full ', ob_broi, 'times' )
else:
    print('Each bucket will be full ', ob_broi, 'times and remainder is 1 l')


    
