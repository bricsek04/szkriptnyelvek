# Egész számok összege 1-től 100-ig

def szamok_osszege(szamok):
    return sum(szamok)

def szamjegyeinek_osszege(szamok):
    osszeg = 0
    for szam in szamok:
        for szamjegy in str(szam):
            osszeg += int(szamjegy)
    return osszeg


def main():
    szamok = list(range(101))
    print(szamjegyeinek_osszege(szamok))
    print(szamok_osszege(szamok))

if __name__ == "__main__":
    main()