# Задача 7
# Вариант 6
"""
Напишите скрипт, позволяющий из исходной строки собрать две новые.
Первая строка должна состоять только из элементов с нечетными индексами исходной строки,
а вторая - с четными.
"""

def split_two_strings_by_idx(input_str):

    builder1 = ""
    builder2 = ""

    for i in range(0, len(input_str)):
        if i % 2:
            builder1 += input_str[i]
        else:
            builder2 += input_str[i]

    return (builder1, builder2)

print(split_two_strings_by_idx("Привет"))
print(split_two_strings_by_idx("123456"))