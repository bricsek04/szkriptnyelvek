import my_math as mm

import random, bullshit

def my_func(s):
    return s[-1]

def main():
    print(mm.triplaz(3))
    print(random.randint(1,3))
    words = ["bb", "cc", "aa", "dd"]
    print(mm.my_choice(words))
    print(bullshit.get_bullshit())

    words2 = ["aa", "ZZ", "bb", "CC", "ab"]
    print(sorted(words2, key=str.lower))
    print(sorted(words2, key=my_func)) # Szövegek rendezése az utolsó kerekterek alapján

if __name__ == "__main__":
    main()