# Задача 45
# Вариант 6

"""

Запишите список в файл посредством модуля pickle и прочитайте его.
"""

import pickle

def writeList(lst):
    with open('data.pkl', 'wb') as f:
        pickle.dump(lst, f)

def readList():
    with open('data.pkl', 'rb') as f:
        return pickle.load(f)

lst = [x for x in range(-100, 100, 3) if x % 9]

writeList(lst)

readedLst = readList()
print(readedLst)

assert lst == readedLst

