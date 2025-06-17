import math

class Kalkulator:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a * self.b

    def oduzimanje(self):
        return self.a - self.b

    def dijeljenje(self):
        if self.b == 0:
            return "Ne mozes dijeliti sa 0"
        return self.a / self.b

    def mnozenje(self):
        return self.a * self.b

    def potenciranje(self):
        return (f"{self.a ** self.b}\n"
               f"{self.b ** self.a}")

    def korijen(self):
        return (f"{math.sqrt(self.a)}\n"
                f"{math.sqrt(self.b)}")

kalkulator = Kalkulator(6,2)

print(kalkulator.korijen())
print(kalkulator.mnozenje())
print(kalkulator.potenciranje())
print(kalkulator.zbroj())
print(kalkulator.dijeljenje())
print(kalkulator.oduzimanje())