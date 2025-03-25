import sys
import random

def from_a_text_file():
    # Чтение текстового документа и занесение строк в массив
    try:
        with open("output.txt", "r", encoding="utf-8") as input_file:
            lines = input_file.readlines()  # Читаем все строки в массив
    except FileNotFoundError:
        print("Файл не найден. Создайте его или проверьте путь.")
        lines = []  # Пустой массив, если файл не найден
    
    #В текстовом файле есть табы и переносы что плохо сказывается на работе программы
    clines = [i.replace("\t\n", "") for i in lines]
    random.shuffle(clines)

    #Фабрика слов
    for i in clines:
        with open(f"{i}.md", "w", encoding="utf-8") as file:
            print(f"Рандомное слово {i}")
            b = str(input('Введите транскрипцию: '))
            print('Введите определение: ')
            c = sys.stdin.read()
            print('Введите пример использования: ')
            d = sys.stdin.read()
            file.write(f"### [{b}]\n")
            file.write("### definition\n")
            file.write(f"{str(c)}\n")
            file.write("---\n")
            file.write(f"{str(d)}\n")
            file.write("[[Word]]\n")
        lines.remove(i+"\t\n")
        with open("output.txt", "w", encoding="utf-8") as file:
            file.writelines(lines)
        g = str(input("Идем дальше или плаки плаки?\n"))
        if g != "да":
            return 0

def with_your_hands():
    # Ввод данных от пользователя
    a = str(input('Введите новое слово: '))
    b = str(input('Введите транскрипцию: '))
    print('Введите определение: ')
    c = sys.stdin.read()
    print('Введите пример использования: ')
    d = sys.stdin.read()

    # Создание .md файла
    with open(f"{a}.md", "w", encoding="utf-8") as file:
        file.write(f"### [{b}]\n")
        file.write("### definition\n")
        file.write(f"{str(c)}\n")
        file.write("---\n")
        file.write(f"{str(d)}\n")
        file.write("[[Word]]\n")
    with_your_hands()

oper = {
    1: from_a_text_file,
    2: with_your_hands,
}

def REVENGE():
    
    i = int(input("Выберите как будем работать:\n\n1. Из текстового файла\n2. Ручками\n\nНу каков ваш ответ? "))
    oper.get(i, 2)()

REVENGE()