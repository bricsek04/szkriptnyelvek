# Egész szám megfordítása

def reverse_number(n):
    return int(str(n)[::-1])

def main():
    number = 1977
    number2 = 12568
    print(reverse_number(number))
    print(reverse_number(number2))

if __name__ == "__main__":
    main()