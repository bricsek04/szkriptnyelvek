#Számjegyek száma

def length_of_number(n):
    return len(str(n))

def main():
    number = 2**256
    print(length_of_number(number))

if __name__ == "__main__":
    main()