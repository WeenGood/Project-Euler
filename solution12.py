#12.Какого первое треугольное число, у которого более пятисот делителей?
def quest12(end = 500):
    i = 0
    triangle = 0
    while 1:
        triangle += i
        count = dividerCounter(triangle)
        if count > end:
            print(triangle)
            return triangle
        #print("Треугольное число номер " + str(i) + " = " + str(triangle) + ". Количество делителей = " + str(count))
        i += 1
    

#Возвращет количество делителей числа num
def dividerCounter(num):
    i = 1
    counter = 0
    while i <= num:
        if num%i == 0:
            counter += 1
        i += 1
    return counter

quest12()