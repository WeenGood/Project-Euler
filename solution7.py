#7.Какое число является 10001-ым простым числом?
def quest7(end = 10001):
    i = 2
    j = 0
    while 1:
        if simpleCheck(i):
            j += 1
        if j == end:
            print(i)
            break
        i += 1

    #проверка на простое число
def simpleCheck(num):
    i = 2
    j = 2
    if num%1 != 0:
        return 0
    while i < num:
        if num%i == 0: 
            j += 1
        if j > 2: 
            return 0
        i += 1
    if j is 2:
        return 1

quest7()
