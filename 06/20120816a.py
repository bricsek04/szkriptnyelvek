# 8 királynő

def sakk(l):
    print("+-----------------+")
    for i in range(8):
        print("|", end=" ")
        for j in range(8):
            if l[j] == 7 - i:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print("|")
    print("+-----------------+")

def main():
    sakk([0,4,7,5,2,6,1,3])

if __name__ == "__main__":
    main()
    