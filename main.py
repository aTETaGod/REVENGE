import sys

def REVENGE():
    a = str(input('Введите новое слово: '))
    b = str(input('Введите транскрипцию: '))
    print('Введите определение: ')
    c = sys.stdin.read()
    print('Введите пример использования: ')
    d = sys.stdin.read()

    with open(f"{a}.md", "w", encoding="utf-8") as file:
        file.write(f"### [{b}]\n")
        file.write("### definition\n")
        file.write(f"{str(c)}\n")
        file.write("---\n")
        file.write(f"{str(d)}\n")
        file.write("[[Word]]\n")
    REVENGE()

REVENGE()