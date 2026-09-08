# Вариант 6
# Задача 41

"""
Напишите скрипт для добавления текста в файл и отображения содержимого файла.
Доработайте скрипт и добавьте функцию-скрипт, подсчитывающий количество строк в файле.
"""

def writeToFileAndOutput(path, text):
    file = open(path, 'a+')

    file.write(text + "\n")

    for line in file:
        print(line)

def countLinesInFile(path):
    file = open(path, 'r')

    return sum(1 for line in file)

filePath = 'task_06.txt'

writeToFileAndOutput(filePath, 'test')
writeToFileAndOutput(filePath, 'hello')

print(countLinesInFile(filePath))



