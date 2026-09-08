# Задача 7
# Вариант 6
"""
Напишите скрипт, позволяющий из исходной строки собрать две новые.
Первая строка должна состоять только из элементов с нечетными индексами исходной строки,
а вторая - с четными.
"""

def process_string(str):

    builder1 = ""
    builder2 = ""

    for i in range(0, len(str)):
        if i % 2:
            builder1 += str[i]
        else:
            builder2 += str[i]

    return (builder1, builder2)

print(process_string("Привет"))
print(process_string("123456"))