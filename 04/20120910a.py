# Hangrend

def hangrend(szo):
    mely_mgh = ['a', 'á', 'o', 'ó', 'u', 'ú']
    magas_mgh = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']
    mely_sz = 0
    magas_sz = 0
    for chr in szo:
        if chr in mely_mgh:
            mely_sz += 1
        if chr in magas_mgh:
            magas_sz +=1
    if magas_sz == 0 and mely_sz != 0:
        return "Mély"
    elif mely_sz == 0 and magas_sz != 0:
        return "Magas"
    elif mely_sz != 0 and magas_sz != 0:
        return "Vegyes"
    else:
        return "Semmilyen"


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pff"]
    for i in words:
        print(hangrend(i))

if __name__ == "__main__":
    main()