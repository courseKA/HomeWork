#4. Съставете програма, която по въведено трицифренo число проверява дали числото се дели на всяка своя цифра.
#Във въведеното число да няма цифра 0.

try:

    num = input('Write a three-digit number: ')

    if int(num)%int(num[0]) == 0 and int(num)%int(num[1]) == 0 and int(num)%int(num[2]) == 0:
        print('The number you entered is divisible by each of its numbers')
    else:
        print('The number you entered is not divisible by each of its numbers')

except:
    print('Enter a three-digit number')