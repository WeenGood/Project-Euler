#2.Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
def quest2():
    a = 0
    b = 1
    c = 0
    summa = 0
    while c < 4000000:
        c = a+b
        if c%2 is 0: summa += c
        a = b
        b = c
    print(summa)
quest2()