# Kivételek #2


def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
        except ValueError:
            print("Hiba: Kérlek, valós számot adj meg!")
            continue
        except ZeroDivisionError:
            print("Hiba: Nullával nem lehet osztani!")
            continue
        except KeyboardInterrupt:
            break
        print('Az osztas eredmenye: {0:.2f}'.format(result))
        print('-' * 10)

#####

if __name__ == "__main__":
    main()