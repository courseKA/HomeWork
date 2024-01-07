# Задача 11. Да се напише програма, която да намира медианата из между три стойности.

num = 7,15,3,6,8,12
dig_num = len(num)
if dig_num % 2 == 0:
    med = (num[dig_num//2 - 1] + num[dig_num//2]) / 2
else:
    med = num[dig_num// 2]
print('Median is: ', med)