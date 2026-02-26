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
    a.index(9)
    a.index(99) # ValueError, mert nincs ilyen elem
    a.append(9)
    a.remove(9) # Az első 9 elemet eltávolítja a listából
    a.remove(9) # ValueError, mert nincs több 9-es elem

    print(sorted(a)) # Rendezett lista, de a eredeti lista nem változik
    # Sorted -> Beépített fgv., meg kell neki adni egy listát, a megadott listát nem módosítja,
    # hanem egy másolatot készít róla és ez fogja randezni, és a végén return-el adja vissza a rendezett másolatot
    print(sorted(a, reverse=True)) # Fordított sorrendben rendezett lista

    a.sort() # Rendezés, nem egy beépített fgv., hanem a lista metódusa, a lista maga lesz rendezve, nem egy új lista jön létre.
    # Nincs visszatérési értéke, None-t ad vissza.
    a.reverse() # Fordított sorrend

    



if __name__ == '__main__':
    main()