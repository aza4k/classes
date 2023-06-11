class Trapecia():
    def __init__(self, a, b,c,d, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h
    def square(self):
        results = (self.a+self.b)*(self.h//2)
        return results
    
    def perimetr(self):
        results = self.a+self.b+self.c+self.d
        return results