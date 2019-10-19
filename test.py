
class one:
    def a(self):
        print("asd")

class two:
    def b (self):
        one.a(self)

qqq = two()
qqq.b()
