#9.Существует только одна тройка Пифагора, для которой a + b + c = 1000. Найдите произведение abc.
#a<b<c a^2 + b^2 = c^2
def quest9(cond = 1000):
    for a in range(0,cond):
        for c in range(0, cond):
            b = cond - a - c
            if a*a + b*b == c*c and a<b and b<c:
                print("a = " + str(a) + " b = " + str(b) + " c = " + str(c))
                print("a*b*c = " + str(a*b*c))

quest9()