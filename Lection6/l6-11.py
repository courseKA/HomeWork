# Задача 11: Да се състави програма, която извежда всички цели числа от интервала [1-
# 50], които удовлетворяват проверка на следното условие:
# c^3 = a^2 + b^2
# Изход:
# Found result: 2^2 + 2^2 = 2^3
# Found result: 2^2 + 11^2 = 5^3
# Found result: 5^2 + 10^2 = 5^3
# Found result: 9^2 + 46^2 = 13^3
# Found result: 10^2 + 5^2 = 5^3
# Found result: 10^2 + 30^2 = 10^3
# Found result: 11^2 + 2^2 = 5^3
# Found result: 16^2 + 16^2 = 8^3
# Found result: 18^2 + 26^2 = 10^3
# Found result: 26^2 + 18^2 = 10^3



for i in range(1,50):
        a = i**2
        for j in range(1,50):
                b = j**2
                for g in range(1,50):
                        c = g**3
                        if a + b == c:
                                print(f"{i}^2 + {j}^2 = {g}^3")
        
           
