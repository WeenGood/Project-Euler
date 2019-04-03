#16. 2**15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26. Какова сумма цифр числа 2**1000?
#считает сумму цифр num
def quest16(num = 2**1000):
    string = str(num)
    i = 0
    summa = 0
    while i < len(string):
        summa += int(string[i])
        i += 1
    return summa

print(quest16())