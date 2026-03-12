# Eltérő viselkedés szimbolikus linken keresztül

# Szimbolikus link létrehozása:
# Lépjünk bele abbak a könyvtárba ami tartalmazza a 20130919a.py fájlt
# Windows: mklink z-a.py 20130919a.py
# Linux: ln -s 20130919a.py z-a.py

import sys

def abc():
    """
        visszaadja az abc stringet
    """
    return('abcdefghijklmnopqrstuvwxyz')

def main():
    """
        A főprogram
    """
    if sys.argv[0] == 'z-a.py':
        print(abc()[::-1])
    else:
        print(abc())

if __name__ == '__main__':
    main()