# Négyzetek összege, összeg négyzete (PE #6)

def negyzetosszeg(szamok):
    osszeg = 0
    for szam in szamok:
        osszeg += szam ** 2
    return osszeg

def osszegnegyzete(szamok):
    return sum(szamok) ** 2

def main():
    szamok = list(range(101))
    print(abs(negyzetosszeg(szamok) - osszegnegyzete(szamok)))

if __name__ == "__main__":
    main()