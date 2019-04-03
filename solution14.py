#14.Какой начальный элемент меньше миллиона сгенерирует самую длинную последовательность? n -> n/2 (n - четное) n -> 3n+1 (n - нечетное)
def quest14(start = 1000000):
    k = 0
    l = 0
    maxL = 0
    maxElem = 0
    while k < start:
        i = start - k
        while i > 1:
            if i%2 == 0:
                i = i/2
            else:
                i = 3*i + 1
            l += 1
        if l > maxL:
            maxL = l
            maxElem = start - k
        l = 0
        k += 1
    print("Максимальная длина последовательности = "+ str(maxL + 1) + " у элемента "+ str(maxElem))
    return maxL + 1

quest14()