TEXT = """
This is a sample text that will be used to demonstrate the functionality of the code. 
The code will process this text and perform various operations on it, such as counting the number of words, finding the frequency of each word, and identifying unique words. 
This text serves as a simple example to illustrate how the code works and to provide a basis for testing its capabilities.
""".strip()
# Stripping leading and trailing whitespace for cleaner output

def main():
    #String operations
    print("'" + TEXT + "'")

    s = "py\n3"
    s2 = r"py\n3" # r menas raw string, so \n is treated as two characters, not a newline
    print(len(s))
    print(len(s2))

    a = [4, 8, 15, 16, 23, 42]
    print(a[0])
    print(a[1])
    print(a[-1])
    print(a[0:2])
    print(a[:2])
    print(a[-2:]) 
    #slicing will be always a new list

    print([1, 2] == [1, 2])

    b = a
    b[0] = 100
    print(a[0])

    b = a[:]
    b[0] = 10
    print(a[0])

    b = a.copy()
    b = []+a

    for var in a:
        print(var)
    # A ciklusváltozó mindig egy másolata lesz a lista elemének

    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    paros = []
    for i in li:
        if i % 2 == 0:
            paros.append(i)
    print(paros)

#------------------------------------

    # Print function
    print("Hello"); print("World")
    print("Hello", end=""); print("World") # end="" means that the next print will be on the same line, without a space

    print(True, 3, "end")
    print(True, 3, "end", sep="---") #Separator between words, default is space

    import sys
    print("Warning!", file=sys.stderr) # Print to standard error instead of standard output

#------------------------------------

    # List operations
    a = [1, 2, 3]
    x = a.pop(1)
    print(x)
    print(a)
    a.pop()
    print(a)

    li = [1, 2, 3, 4, 5]
    li.append(6)
    li.pop()
    # Verem

    li.append(7)
    li.pop(0) # Kölstéges, mert a lista elejét kell eltolni
    # Sor

#------------------------------------

    # Gyakori lista műveletek

    li = [1, 2, 3, 4, 5]
    
    # Szúrjuk be az 5-öt a 2 és 8 közé
    li.insert(2, 5)
    print(li)

    # Szúrjuk be a 100-at a 9-es elé
    li.insert(-1, 100)
    print(li)

    # Szúrjuk be a b listát az a listába
    b = [6, 7, 8]
    a.append(b) # a listába kerül a b lista, mint egyetlen elem
    print(a)
    a.pop()
    a.extend(b) # a listába kerülnek a b lista elemei külön-külön
    print(a)

    # Keressük meg a 9-es elemet a listában
    a.index(8)
    try:
        a.index(99) # ValueError, mert nincs ilyen elem
    except ValueError:
        print("Elem nem található")
    a.append(9)
    a.remove(9) # Az első 9 elemet eltávolítja a listából
    try:
        a.remove(99) # ValueError, mert nincs ilyen elem
    except ValueError:
        print("Elem nem található")

    print(sorted(a)) # Rendezett lista, de a eredeti lista nem változik
    # Sorted -> Beépített fgv., meg kell neki adni egy listát, a megadott listát nem módosítja,
    # hanem egy másolatot készít róla és ez fogja randezni, és a végén return-el adja vissza a rendezett másolatot
    print(sorted(a, reverse=True)) # Fordított sorrendben rendezett lista

    a.sort() # Rendezés, nem egy beépített fgv., hanem a lista metódusa, a lista maga lesz rendezve, nem egy új lista jön létre.
    # Nincs visszatérési értéke, None-t ad vissza.
    a.reverse() # Fordított sorrend

#------------------------------------
    # 4. Hét

    li = [1, 2, 3, 4, 5]
    print(max(li))
    print(min(li))
    print(sum(li))

    import math
    print(math.prod(li)) # Szorzat

    words = ["aa", "bb", "cc", "dd", "ee"]
    print(":".join(words)) # "aa:bb:cc:dd:ee" stringet ad vissza

    s = "aa:bb:cc:dd:ee"
    print(s.split(":")) # ["aa", "bb", "cc", "dd", "ee"] listát ad vissza

    s = "   aa   bb   cc   dd   ee   "
    print(s.split()) # ["aa", "bb", "cc", "dd", "ee"] listát ad vissza, a split() alapértelmezetten whitespace karakterekre bontja a stringet, és eltávolítja a leading és trailing whitespace karaktereket

    range(10) # 0-tól 10-ig
    range(1, 10) # 1-től 10-ig
    range(5, 10, 2) # 5-től 10-ig, 2-es lépésközzel, azaz 5, 7, 9
    # a range egy iterátor, nem egy lista, ezért nem lehet indexelni, de lehet listává alakítani: list(range(10))

    print(list(range(98, 82, -1)))

    print(sum(range(101)))

    ord("a") # 97, a karakter ASCII kódja
    chr(97) # "a", a karakter ASCII kódja alapján visszaadja a karaktert

    bool(0) # False
    bool(0.2) # True
    bool("") # False
    bool("asd") # True, mert nem üres string
    bool([]) # False
    bool([1, 2, 3]) # True, mert nem üres lista
    bool(None) # False
    bool(False) # False
    bool(True) # True

    li = []
    if li: # A lista üres, akkor False, egyébként True
        print("A lista nem üres")

    if not li: # A lista üres, akkor True, egyébként False
        print("A lista üres")

    import this # A Zen of Python, a Python filozófiája, amit Tim Peters írt, és a Python fejlesztői követnek, hogy a kódjuk egyszerű, olvasható és karbantartható legyen.

    # Tuple adatszerkezet, nem módosítható lista, zárójelek között, elemek vesszővel elválasztva
    t = (1, 2, 3)
    type(t) # <class 'tuple'>
    len(t) # 3
    t[0] # 1
    t[0:2] # (1, 2)
    t[-2:] # (2, 3)
    
    m = ("Total recall", 1990, 8.3)
    print(m)
    # A tuple kezelhető heterogén adatszerkezetként, azaz különböző típusú elemeket is tartalmazhat.

    # Párhuzamos értékadás
    x, y = 3,5
    (x, y) = (3, 5) # Ez a forma is működik, a bal oldalon egy tuple van, a jobb oldalon egy tuple, és a két tuple elemei párhuzamosan értékadódnak.

    a = 5
    b = 10
    a, b = b, a # A két változó értékét megcseréljük.

    t = (1,) # Egy elemű tuple, a vessző kötelező, különben nem lesz tuple, hanem egy sima érték lesz zárójelek között.

    



if __name__ == '__main__':
    main()