from math import pi


class Krug:
    r = 0

    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * self.r * pi

    def povrsina(self):
        return (self.r ** 2) * pi

krug = Krug(3)
print(krug.opseg())
print(krug.povrsina())