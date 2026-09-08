# 46 Задача
# Вариант 6

"""
Запишите словарь в файл посредством модуля json и прочитайте его.
"""

import json

def writeDict(dict):
    with open('employee.json', 'w') as f:
        json.dump(dict, f)

def readDict():
    with open('employee.json', 'r') as f:
        return json.load(f)

dict = {
    "Alice": "Programmer",
    "Bob": "System Architect",
    "Jeb": "Data Analytic"
}


writeDict(dict)
readedDict = readDict()
print(readedDict)

assert dict == readedDict