# Egész szám megfordítása

def reverse_number(n):
    reversed_string = str(n)[::-1]
    return int(reversed_string)

def main():
    number = 1977
    number2 = 12568
    print(reverse_number(number))
    print(reverse_number(number2))

if __name__ == "__main__":
    main()