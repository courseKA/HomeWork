#2. Да се състави програма, чрез която се въвеждат 2 естествени двуцифрени числа a,b. Програмата да изведе съобщение 
#дали последната цифра от произведението на двете числа е четна, както и самата цифра. Входни данни: 
#a,b - естествени числа от интервала [10..99].

try:
    num1 = input('Write number between 10 and 99: ')
    num2 = input('Write number between 10 and 99: ')
    num3 = int(num1) * int(num2)
    if num3%2 == 0:
        print('Number is even')
    else:
        print('Number is odd')
    num4 = str(num3)
    last_digit = num4[-1]
    if int(last_digit)%2 == 0:
        print('the last number is even')
    else:
         print('Last number is odd')
except:
     print('Write correct number')