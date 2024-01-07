#5. Да се състави програма, която да изчислява периметър и площ на
#правоъгълник по въведени дължини на прилежащи страни - естествени числа от интервала [5 ..100]. 
#Изведете съобщение, ако страните формират квадрат.

a = int(input('Enter digit between 5 and 100: '))
b = int(input('Enter digit between 5 and 100: '))
perimeter = 2 * a + 2 * b
print('Perimeter is: ', perimeter)
ploshta = a * b
print("Figure's area is: ", ploshta)
if a == b:
    print('The figure is square.')