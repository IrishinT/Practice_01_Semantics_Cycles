# 19 задача
# Вариант 6

"""
Напишите скрипт для слияния (конкатенации) двух списков различными способами.
"""

def sumListsByOperator(lst1, lst2):
    return lst1 + lst2


def sumListsByCycle(lst1, lst2):
    result = []

    for el1 in lst1:
        result.append(el1)


    for el2 in lst2:
        result.append(el2)

    return result

print(sumListsByCycle([1,2,3], [4,5,6]))
print(sumListsByCycle(['123', '456'], ['qwerty']))