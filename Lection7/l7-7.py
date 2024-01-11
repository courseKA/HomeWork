'''Задача 7. Напишете програма, която намира максимална редица от последователни
еднакви елементи в списък.
Пример: {2, 1, 1, 2, 3, 3, 2, 2, 2, 1} -> {2, 2, 2}. ‘2’ * counter'''

lst = [2,1,1,2,3,3,2,2,2,1]
# Create empty list
duplicates = []
res = []
# Find equal digits
for numb in lst:
    if not duplicates:
        duplicates.append(numb)
    else:
        if numb == duplicates[0]:
            duplicates.append(numb)
        elif numb != duplicates[0]:
            duplicates.clear()
            duplicates.append(numb)
        
    if len(res) < len(duplicates):
        res = duplicates.copy()

print(res)
