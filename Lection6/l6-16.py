# Задача 16. Да се създаде програма, която да въвежда текст от клавиатурата и да
# премахва повтарящите се букви в текста.
# Вход: aaabbbccc
# Изход: abc

text = 'aaabbbcc'
n_t = ''
for i in text:
    if i not in n_t:
        n_t = n_t + i
print(n_t)
