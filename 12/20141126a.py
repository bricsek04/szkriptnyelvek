# palindrom két számrendszerben is (PE #36)

def is_palindrome(s):
    return s == s[::-1]

def palindrome2():
    osszeg = 0
    for n in range(1, 1000000):
        decimalis = str(n)
        if is_palindrome(decimalis):
            binaris = bin(n)[2:]
            if is_palindrome(binaris):
                osszeg += n
    return osszeg

def main():
    print(palindrome2())

if __name__ == "__main__":
    main()