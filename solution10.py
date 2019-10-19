#10.Найдите сумму всех простых чисел меньше двух миллионов.
def quest10(end = 2000000):
    i = 2
    summa = 0
    while(i <= end):
        if simpleCheck(i) == 1:
            summa += i
        i += 1
    print(summa)

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

quest10()