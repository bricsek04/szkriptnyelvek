# Münchausen-számok

def münchausen_numbers(numbers):
    """
        Münchausen-számok keresése

        Paraméter:
            numbers (iterable): A számokat tartalmazó iterálható objektum

        Visszatérési érték:
            list: A Münchausen-számok listája
    """
    münchausen_numbers = []
    su = 0
    for i in numbers:
        if i == 0:
            münchausen_numbers.append(i)
        for c in str(i):
            su += int(c)**int(c)
        if su == i:
            münchausen_numbers.append(i)
        su = 0
    return münchausen_numbers

def main():
    """
        A főprogram
    """
    print(münchausen_numbers(range(10001)))

if __name__ == '__main__':
    main()