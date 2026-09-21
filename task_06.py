# Вариант 6
# Задача 41

"""
Напишите скрипт для добавления текста в файл и отображения содержимого файла.
Доработайте скрипт и добавьте функцию-скрипт, подсчитывающий количество строк в файле.
"""

def writeToFileAndOutput(path, text):
    with open(path, 'a+', encoding='utf-8') as file:
        file.write(text + "\n")
        file.seek(0)

        for line in file:
            print(line)

def countLinesInFile(path):
    with open(path, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)

filePath = 'task_06.txt'

writeToFileAndOutput(filePath, 'test')
writeToFileAndOutput(filePath, 'hello')

print(countLinesInFile(filePath))



