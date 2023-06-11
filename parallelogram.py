class Parallel():
    def __init__(self, a,b,h):
        self.a = a
        self.b = b
        self.h = h
    def square(self):
        result = self.a * self.h
        return result
    def perimetr(self):
        result = (self.a + self.b)*2
        return result