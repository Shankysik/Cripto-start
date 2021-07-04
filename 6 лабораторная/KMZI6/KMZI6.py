def shift(lst,steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
    return lst

def gamma(bin, vector1):
    x = 0
    print("Такт", x, ": ", vector1)
    while (x < 12):
        i = 0
        last_item = vector1[-1]

        if (x == 0):
            gamma = [last_item]
        else:
            gamma.append(last_item)

        while(i < len(bin)-1):
            if(bin[i] == "1"):
                vector1[-1] = str(int(vector1[i]) ^ int(vector1[-1]))
            i += 1
        x += 1
        vector1 = shift(vector1, 1)
        print("Такт", x, ": ", vector1)
    return gamma
def gammamore(bilist, init_vect):
    x = 0
    #print("Такт", x+1, ": ", init_vect)
    taktarov = ""
    while (x < 105):
        i = 0
        last_num = init_vect[7]
        if(x == 0):
            gamma = [last_num]
        else:
            gamma.append(last_num)
        while(i < len(bilist)-1):
            if(bilist[i] == '1'):
                init_vect[-1] = str(int(init_vect[i]) ^ int(init_vect[-1]))
            i += 1
        init_vect = shift(init_vect, 1)
        if(x>=99 and x<104):
            print("Такт", x+2, ": ", init_vect)
        if(x>=100 and x<106):
            taktarov += last_num
        x += 1
    return taktarov


def xoring(op_text, gamma):
    i = 0
    crypt_text = []
    while(i < len(op_text)):
        if(op_text[i] == gamma[i]):
            crypt_text.append('0')
        else:
            crypt_text.append('1')
        i += 1
    return crypt_text

a = int(input("Введите порождающий многочлен в 16-ричной системе : "), (16))
b = bin(a)[2:]
print("Многочлен в 2-ой системе счисления ---------------- "+b)
b = b[::-1]  # переворот строки
b = b[1:]
b = list(b)
vector1 = input("Введите первый вектор инициализации: ")
vector1 = list(vector1)
gamma = gamma(b, vector1)
print("Полученная гамма: " + str(''.join(gamma)))
message = input('Введите сообщение для шифровки: ')
message = list(message)
print('Зашифрованный текст: ' + "".join(xoring(message, gamma)))
vector2 = input("Введите второй вектор инициализации: ")
vector2 = list(vector2)
second_gamma = gammamore(b, vector2)
print("Значения выходных битов псевдослучайной последовательности в течение 101 – 105 тактов: " + ', '.join(second_gamma))
input('Для завершения работы нажмите любую клавишу...')