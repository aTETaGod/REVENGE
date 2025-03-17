import sys

a = str(input('Введите новое слово: '))
b = str(input('Введите транскрипцию: '))
print('Введите определение: ')
c = sys.stdin.read()
print('Введите пример использования: ')
d = sys.stdin.read()

print(c)

with open(f"{a}.md", "w", encoding="utf-8") as file:
    file.write(f"### [{b}]\n\n")
    file.write("### definition\n\n")
    file.write(f"{str(c)}\n\n")
    file.write("---\n\n")
    file.write(f"{str(d)}\n\n")
    file.write("[[Word]]\n")
