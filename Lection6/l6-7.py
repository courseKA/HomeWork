#Задача 7. Да се напише програма, която принтира редицата на Фибуначи между 0 и 50.
#Редицата на Фибуначи е: 0, 1, 1, 2, 3, 5, 8, 13, 21, … Всяко следващо число е сумата от
#предходните две.
   
x=0
y=1
while x <= 50:
    print(x)
    z = y
    y = x
    x = z + y


#SECOND DECISION
n = int(input ("Enter the number you want to print: "))     
# Take input from user that how many numbers you want to print  
a = 0    
b = 1    
for i in range(0,n):  
    print(a, end = " ")             # a:0;    a:1;       a:2  
    c = a+b                     #c=0+1=1; c= 1+1=2;  c=1+2=3  
    a = b               #a=1    ; a=1;       a=2  
    b = c               #b=1    ; b=2;       b=3  
