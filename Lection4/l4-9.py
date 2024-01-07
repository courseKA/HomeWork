#Задача 9. Да се напише програма, която да превръща температура от целзий във фаренхайт.
#Формулата е следната: T (° F) = T (° C) × 1.8 + 32, където c е температурата в целзий и f температурата в
#фаренхайт.
#Примерен изход:
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius

t = float(input('Write temperture in Celsius:  '))

tf = t * 1.8 + 32
print('Tempeture in Fahrenheit is: ', tf)