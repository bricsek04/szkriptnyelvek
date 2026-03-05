# Diamond

def diamond(magassag):
    if magassag % 2 == 0:
        print("Páros magasság nem elfogadott!")
    else:
        for i in range(magassag):
            stars = 2 * min(i, magassag - 1 - i) + 1
            row = "*" * stars
            print(row.center(magassag))


def main():
    magassag = 7
    diamond(magassag)

if __name__ == "__main__":
    main()