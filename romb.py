class Romb():
    def __init__(self, a,h):
        self.a =a
        self.h = h
    def square(self):
        result = self.a * 4
        return result
    def perimetr(self):
        result = self.a * self.h
        return result