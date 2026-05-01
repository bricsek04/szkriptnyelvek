# nyomtatandó oldalak

def nyomtatas(s: str) -> list:
    oldalak = s.split(',')
    nyomtatando = []
    for oldal in oldalak:
        if '-' in oldal:
            start, end = oldal.split('-')
            nyomtatando.extend(range(int(start), int(end)+1))
        else:
            nyomtatando.append(int(oldal))
    return nyomtatando

def main() -> None:
    be = input("Kérem adja meg a nyomtatandó oldalakat pl.: 1-4,7,9,11-15 : ")
    print(nyomtatas(be))

if __name__ == "__main__":
    main()