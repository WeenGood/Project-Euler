#3.Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''
def quest3():
    num = 600851475143
    divider = 0
    i = 1
    while i <= num:
        while simpleCheck(i) is 0 and i<=num:
            i += 1
        if num%i is 0 and i > divider:
            divider = i
        i += 1
    print(divider)
'''
def quest3(num = 600851475143):
    j = 2
    i = num
    while not simpleCheck(i):
        i = num / j
        j += 1
    print(i)

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

quest3()