#5.Какое самое маленькое число делится нацело на все числа от 1 до 20?
def quest5(start = 1, end = 20):
    i = end
    while 1:
        if divineCheck(i,start,end):
            print(i)
            break
        i += 20

#проверка на деление нацело
def divineCheck(num, start, end):
    j = 0
    nm = range(start,end)#[2,3,5,7,11,13,17,19]
    for a in nm:
        if num%a == 0: 
            j += 1
            continue
        else: return 0
    if j == len(nm):
        return 1

quest5()