# Palindróm (iteratív és rekurzív változat)

# Iteratív módszer. A sztringről nem készíthetünk másolatot.
def is_palindrome_iterative(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]: # -i-1 a -1, -2, -3, ... indexeket adja
            return False
    return True

# Rekurzív módszer. Csak hogy szokjuk a rekurziót is.
def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

def main():
    s = "hello"
    s2 = "racecar"
    print(is_palindrome_iterative(s))
    print(is_palindrome_iterative(s2))
    print(is_palindrome_recursive(s))
    print(is_palindrome_recursive(s2))

if __name__ == "__main__":
    main()