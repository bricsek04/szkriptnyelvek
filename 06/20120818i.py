# Számjegyek összege (PE #16)

def szamjegyek_osszege(szam):
    osszeg = 0
    for s in str(szam):
        osszeg += int(s)
    return osszeg

def main():
    print(szamjegyek_osszege(2**1000))

if __name__ == "__main__":
    main()