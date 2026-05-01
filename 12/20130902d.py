#Prím palindrom

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def test(n):
    while True:
        if is_palindrome(n) and is_prime(n):
            return n
        n += 1

if __name__ == "__main__":
    print(test(31))
    print(test(130))
    print(test(131))
    print(test(1977))