from colorama import init,Fore, Back, Style
init(autoreset = 1)
def key_input_exception():
    try:
        key_input = input("Введите 10 бит ключа: ")
    except ValueError:
        return print(Fore.RED + Style.BRIGHT + "В последовательности бит не может быть букв")
    if (len(key_input) == 10):
        for i in key_input:
            if ((i != '1') and (i != '0')):
                print(Fore.RED + Style.BRIGHT + "В последовательности бит могут быть только 0 и 1")
                return None
            else:
                continue
        return key_input
    else:
        print(Fore.RED + Style.BRIGHT + "Ключ должен состоять из 10 бит")
        return None

def message_input_exception():
    try:
        message_input = input("Введите 8 бит сообщения: ")
    except ValueError:
        return print(Fore.RED + Style.BRIGHT + "В последовательности бит не может быть букв!")
    if (len(message_input) == 8):
        for i in message_input:
            if ((i != '1') and (i != '0')):
                print(Fore.RED + Style.BRIGHT + "В последовательности бит могут быть только 0 и 1")
                return None
            else:
                continue
        return message_input
    else:
        print(Fore.RED + Style.BRIGHT + "Сообщение должно состоять из 8 бит")
        return None

def keys_generation(key_global):
    p10 = [[key_global[2], key_global[4], key_global[1], key_global[6], key_global[3]],
           [key_global[9], key_global[0], key_global[8], key_global[7], key_global[5]]]
    shift(p10[0],-1)
    shift(p10[1],-1)
    p81 = [p10[1][0], p10[0][2], p10[1][1], p10[0][3], p10[1][2], p10[0][4], p10[1][4], p10[1][3]]
    shift(p10[0],-2)
    shift(p10[1],-2)
    p82 = [p10[1][0], p10[0][2], p10[1][1], p10[0][3], p10[1][2], p10[0][4], p10[1][4], p10[1][3]]
    return p81, p82

def shift(lst,steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

def encryption(mes_global, key1, key2):
    ip = [mes_global[1], mes_global[5], mes_global[2], mes_global[0], mes_global[3], mes_global[7], mes_global[4], mes_global[6]]
    ip_l = [ip[0], ip[1], ip[2], ip[3]]
    ip_r = [ip[4], ip[5], ip[6], ip[7]]
    fk1 = fk_func(ip_r, ip_l, key2)
    so_close = fk_func(fk1, ip_r, key1)
    reverse_ip = [so_close[3], so_close[0], so_close[2], fk1[0], fk1[2], so_close[1], fk1[3], fk1[1]]

    print(Back.CYAN + Style.BRIGHT + ''.join(reverse_ip))

def fk_func(ip_r, ip_l, key):
    ep = [ip_r[3], ip_r[0], ip_r[1], ip_r[2], ip_r[1], ip_r[2], ip_r[3], ip_r[0]]
    i = 0
    xor = ''
    while i < len(ep):
        if (ep[i] == key[i]):
            xor += xor.join('0')
        else:
            xor += xor.join('1')
        i +=1
    xor1 = xor[0]+xor[1]+xor[2]+xor[3]
    xor2 = xor[4]+xor[5]+xor[6]+xor[7]
    s0 = [['1', '0', '3', '2'],
          ['3', '2', '1', '0'],
          ['0', '2', '1', '3'],
          ['3', '1', '3', '1']]

    s1 = [['1', '1', '2', '3'],
          ['2', '0', '1', '3'],
          ['3', '0', '1', '0'],
          ['2', '1', '0', '3']]
    stroka1 = xor1[0] + xor1[3]
    stolbe1 = xor1[1] + xor1[2]
    stroka2 = xor2[0] + xor2[3]
    stolbe2 = xor2[1] + xor2[2]

    if (s0[int(stroka1, 2)][int(stolbe1, 2)] == '3'):         #Следить внимательно за этой паскудой!
        S00 = ['1', '1']
    elif (s0[int(stroka1, 2)][int(stolbe1, 2)] == '2'):         #Следить внимательно за этой паскудой!
        S00 = ['1', '0']
    elif (s0[int(stroka1, 2)][int(stolbe1, 2)] == '1'):         #Следить внимательно за этой паскудой!
        S00 = ['0', '1']
    elif (s0[int(stroka1, 2)][int(stolbe1, 2)] == '0'):         #Следить внимательно за этой паскудой!
        S00 = ['0', '0']

    if (s1[int(stroka2, 2)][int(stolbe2, 2)] == '3'):         #Следить внимательно за этой паскудой!
        S11 = ['1', '1']
    elif (s1[int(stroka2, 2)][int(stolbe2, 2)] == '2'):         #Следить внимательно за этой паскудой!
        S11 = ['1', '0']
    elif (s1[int(stroka2, 2)][int(stolbe2, 2)] == '1'):         #Следить внимательно за этой паскудой!
        S11 = ['0', '1']
    elif (s1[int(stroka2, 2)][int(stolbe2, 2)] == '0'):         #Следить внимательно за этой паскудой!
        S11 = ['0', '0']

    p4 = [S00[1], S11[1], S11[0], S00[0]]
    i = 0
    p4_xored = ''
    while i < len(p4):
        if (p4[i] == ip_l[i]):
            p4_xored += p4_xored.join('0')
        else:
            p4_xored += p4_xored.join('1')
        i +=1
    return p4_xored

running = True
while(running == True):
    while(True):
        key = key_input_exception()
        if(key == None):
            print("Введите ключ ")
            continue
        else:
            k1, k2 = keys_generation(key)
            break
    while(True):
        message = message_input_exception()
        if(message == None):
            print("Введите слово")
            continue
        else:
            ip1 = encryption(message, k1, k2)
            break
    answer = input("Выйти? (y/n): ")
    while(True):
        if(answer == 'y'):
            running == False
            sys.exit()
            break
        elif(answer == 'n'):
            running == True
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Выберите правильный вариант ответа")
            continue