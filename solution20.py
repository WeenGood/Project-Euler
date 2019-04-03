#20. Найдите сумму цифр в числе 100!.
def quest20(end = 100):
    fact = factorial(end)
    string = str(fact)
    i = 0
    summa = 0
    while i < len(string) - 1:
        summa += int(string[i])
        i += 1
    print(summa)

#Считает факториал end!
def factorial(end = 100):
    i = 1
    answer = 1
    while i <= end:
        answer *= i
        i += 1
    return answer

quest20()