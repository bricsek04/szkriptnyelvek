# Palindróm

def is_palindrome(s):
    return s == s[::-1]

def main():
    print(is_palindrome("racecar"))
    print(is_palindrome("hello"))

if __name__ == "__main__":
    main()