# Sphere (gömb) és Ellipse (ellipszis) osztályok megírása; a Sphere osztály esetén terheljük túl a következő operátorokat: <, <=, >, >=.

import math


class Sphere:
    def __init__(self, r):
        self.r = r

    def felszin(self):
        return 4*math.pi*(self.r**2)

    def kerület(self):
        return 2*math.pi*self.r

    def terfogat(self):
        return (4/3) * math.pi * (self.r**3)

    def __lt__(self, other):
        return self.terfogat() < other.terfogat()
    
    def __gt__(self, other):
        return self.terfogat() > other.terfogat()
    
    def __le__(self, other):
        return self.terfogat() <= other.terfogat()
    
    def __ge__(self, other):
        return self.terfogat() >= other.terfogat()


class Ellipse:
    def __init__(self, a ,b):
        self.a = a
        self.b = b
    
    def terület(self):
        return math.pi * self.a * self.b

def main():
    s = Sphere(3)
    print(s.felszin())
    print(s.kerület())
    print(s.terfogat())
    s2 = Sphere(6)
    s3 = Sphere(3)

    print(s > s2)
    print(s < s2)
    print(s <= s3)
    print(s <= s3)

    e = Ellipse(3, 6)
    print(e.terület())


if __name__ == "__main__":
    main()