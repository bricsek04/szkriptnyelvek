# Lista elemeinek szorzata

def lista_szorzata(li):
    prod = 1
    for i in li:
        prod *= i
    return prod

def main():
    li = [1,2,3,4,5]
    li2 = []
    print(lista_szorzata(li))
    print(lista_szorzata(li2))

if __name__ == "__main__":
    main()