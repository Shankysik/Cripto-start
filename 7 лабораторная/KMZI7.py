def secret_key(p, a):
    i = 1
    while True:
        if (((p - 1) * i) + 1) % a == 0:
            prikol = (((p - 1) * i) + 1) // a
            break
        else:
            i += 1
    return prikol


def crypting(m, p, stepen):
    mesage = (m ** stepen) % p
    return mesage


p = int(input("Введите кодирующие число: "))
a = int(input("Ведите придуманный ключ а: "))
b = int(input("Ведите придуманный ключ b: "))
alpha = secret_key(p, a)
betta = secret_key(p, b)
print("Первый секретный ключ a - " + str(alpha))
print("Второй секретный ключ b - " + str(betta))
m = int(input("Введите шифруемое число: "))
step1 = crypting(m, p, a)
print("Сообщение секретный ключ a - " + str(step1))
step2 = crypting(step1, p, b)
print("Сообщение секретный ключ b - " + str(step2))
step3 = crypting(step2, p, alpha)
print("Сообщение секретный ключ alpha - " + str(step3))
step4 = crypting(step3, p, betta)
print("Сообщение секретный ключ betta - " + str(step4))
input("Нажмите любую клавищу для завершеия работы...")
