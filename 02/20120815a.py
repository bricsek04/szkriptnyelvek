# Két szám összege

import sys

def sum_a(num1, num2):
    if num1 is None or num2 is None:
        return "Nem adta meg mind 2 számot"
    return int(num1) + int(num2)

def sum_b(num1, num2):
    return num1 + num2

def main():
    print(sum_a(sys.argv[1], sys.argv[2]))
    num1 = int(input("Add meg az első számot: "))
    num2 = int(input("Add meg a második számot: "))
    print(sum_b(num1, num2))

if __name__ == "__main__":
    main()