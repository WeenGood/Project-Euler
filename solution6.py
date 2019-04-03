import math
#6.Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел
def quest6(start = 0,end = 100):
    i = start
    summaSquads = 0
    summa = 0
    while i <= end:
        summa += i
        summaSquads += i*i
        i += 1
    print(math.fabs(summaSquads - summa*summa))

quest6("-10",-5)