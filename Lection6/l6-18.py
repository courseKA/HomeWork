# Задача 18. Да се напише програма, която да приема като вход текст и да намира
# количеството повтарящи се знаци в текста. Включват се интервалите и текста трябва да е с малки
# букви. Ако няма дубликати, да се принтира 0.
# Вход: Hello World!
# Изход: 3
# Вход: foobar
# Изход: 1
# Вход: birthday
# Изход: 0
# Вход: helicopter
# Изход: 1

text = 'Hello World'
n_text = text.lower()
new = set(n_text)
sum = 0
for i in new:
    count_s = n_text.count(i)
    if count_s > 1:
        sum += count_s - 1
print(sum)