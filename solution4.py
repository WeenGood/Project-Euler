#4.Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
def quest4():
    start = 100
    end = 999
    i = start
    j = start
    maxMult = 0
    while len(str(i)) <= len(str(end)):
        while len(str(j)) <= len(str(end)):
            mult = i * j
            if palindromCheck(mult) and mult > maxMult:
                maxMult = mult
            j += 1
        i += 1 
        j = start
    print(maxMult)

    #проверка на палиндром
def palindromCheck(num):
    strNum = str(num)
    i=0
    j=0
    while i<=len(strNum)-1:
        if strNum[i] == strNum[len(strNum)-1-i]:
            j += 1
        else: break
        i += 1
    if j == len(strNum): return 1
    return 0

quest4()
#print(palindromCheck("1233333"))