#1.Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
def quest1():
    i = 0
    summa = 0
    while i<1000:
        if i%3 is 0 or i%5 is 0: summa += i
        i+=1
    print(summa)
quest1()