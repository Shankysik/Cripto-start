from colorama import init, Fore, Back, Style
init(autoreset=1)

alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя_'

def Crypt():
    kriptworld = []
    for ind, item in enumerate(wordidex):
        kriptworld.append(alf[(((item + keyindex[(ind % len(keyindex))]) + offset) % len(alf))])
    return kriptworld


def DeCrypt():
    norm = []
    for ind, item in enumerate(wordidex):
        norm.append(alf[(((item - keyindex[(ind % len(keyindex))]) + len(alf) - offset) % len(alf))])
    return norm

while True:
    keyindex = []
    wordidex = []
    offset = 0
    way = int(input("Выберете действие:\n 1)Зашифровать\n 2)Расшифровать\n 3) Выйти\n"))
    if way == 3:
        print(Fore.RED + Style.BRIGHT + 'Конец работы')
        break
    word = input('Введите исходную фразу: ')
    key = input('Введите ключ шифрования: ')
    offset = input('Укажите размер смещения: \n 1)ROT0 - "a" преобразуется в "а"\n 2)ROT1 - "a" преобразуется в "б"\n')
    if offset == '1':
        offset = 0
    elif offset == '2':
        offset = 1
    else:
        print(Fore.RED + Style.BRIGHT + "Размер смещения задан некоретно")
        continue

    for i in word:
        wordidex.append(alf.find(i))

    for i in key:
        keyindex.append(alf.find(i))

    if way == 1:
        print(Back.CYAN + Style.BRIGHT + ''.join(Crypt()))
    elif way == 2:
        print(Back.CYAN + Style.BRIGHT + ''.join(DeCrypt()))
    else:
        print(Fore.RED + Style.BRIGHT + "Введите коретные данные выбора действия")
        continue