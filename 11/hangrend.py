# korábbi hangrendes feladat megoldása Enum használatával (7. fólia vége)

from enum import Enum

class HangrendTipus(Enum):
    MELY = "Mély"
    MAGAS = "Magas"
    VEGYES = "Vegyes"
    SEMMILYEN = "Semmilyen"

def hangrend(szo):
    mely_mgh = ['a', 'á', 'o', 'ó', 'u', 'ú']
    magas_mgh = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']
    mely_sz = 0
    magas_sz = 0
    
    for betu in szo:
        if betu in mely_mgh:
            mely_sz += 1
        if betu in magas_mgh:
            magas_sz += 1
            
    if magas_sz == 0 and mely_sz != 0:
        return HangrendTipus.MELY
    elif mely_sz == 0 and magas_sz != 0:
        return HangrendTipus.MAGAS
    elif mely_sz != 0 and magas_sz != 0:
        return HangrendTipus.VEGYES
    else:
        return HangrendTipus.SEMMILYEN


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pff"]
    for szo in words:
        eredmeny = hangrend(szo)
        print(f"{szo}: {eredmeny.value}")

if __name__ == "__main__":
    main()