#17.Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв. Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
'''
Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам британского английского.
'''



def quest17():
    words1 = ["","one","two","three","four","five","six","seven","eight","nine"]
    words11 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    words2 = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    words3 = ["hundred","thousand"]

    i = 1
    text = ""

    while i<10:
        text += words1[i] + " "
        i+=1
    text += words2[1] + " "
    i+= 1
    while i<20:
        text+= words11[i-11]+ " "
        i+=1
        
    while i!=100:   
        text += words2[(i//10)] + " " + words1[i%10] + " "
        i+=1

    while i!=1000:
        text += words1[i//100] + " " + words3[0] + " "
        if i%100 != 0:
            if (i-(i//100)*100)//10 == 1:
                if i%10 == 0:
                    text += "and " + words2[1] + " "
                else:
                    text += "and " + words11[i%10-1] + " "
            else:
                text+= "and " + words2[(i-(i//100)*100)//10] + " " + words1[i%10] + " "
        i+=1
    text += "one " + words3[1]
    res = len(text)
    print(text)
    text = text.replace(" ","")
    res = len(text)
    print(res)


quest17()