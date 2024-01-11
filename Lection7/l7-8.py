'''Задача 8. Напишете програма, която намира максималната редица от последователни
нарастващи елементи в списък.
Пример: {3, 2, 3, 4, 2, 2, 4} -> {2, 3, 4}.'''

lst = [3, 2, 3, 4, 2, 2, 4, 5, 6, 7]
lst_posledovatelni = []
res = []

for numb in range(len(lst)):
    if lst[numb -1] < lst[numb] and lst[numb] - lst[numb -1] == 1:
        lst_posledovatelni.append(lst[numb])
        
    elif lst[numb -1]  > lst[numb] or lst[numb] - lst[numb -1] > 1:
            lst_posledovatelni.clear()
            lst_posledovatelni.append(lst[numb])
    if len(res) < len(lst_posledovatelni):
        res = lst_posledovatelni.copy()
print(res)
