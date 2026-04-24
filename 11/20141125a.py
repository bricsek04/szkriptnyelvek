# Verem és sor megvalósítása saját osztállyal

class Verem:
    def __init__(self):
        self.verem = []
    
    def __str__(self):
        return str(self.verem)

    def ures(self):
        if self.verem:
            return False
        else:
            return True
    
    def betesz(self, ertek):
        self.verem.append(ertek)

    def kivesz(self):
        if self.verem:
            return self.verem.pop()
        else:
            return None

    def meret(self):
        return len(self.verem)

class Sor:
    def __init__(self):
        self.sor = []

    def __str__(self):
        return str(self.sor)

    def ures(self):
        if self.sor:
            return False
        else:
            return True

    def betesz(self, ertek):
        self.sor.append(ertek)

    def kivesz(self):
        if self.sor:
            return self.sor.pop(0)
        else:
            return None

    def meret(self):
        return len(self.sor)


def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)

    print("------------------------")

    s = Sor()
    print(s)
    print(s.ures())
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)
    print(s.meret())
    print(s.ures())
    x = s.kivesz()
    print(x)
    print(s)
    s.kivesz()
    s.kivesz()
    x = s.kivesz()
    print(x)

if __name__ == "__main__":
    main()