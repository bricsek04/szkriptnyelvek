# AoC2017, Day 4, Part 1 (High-Entropy Passphrases)

def is_passphrase(passphrase):
    passphrase = passphrase.split()
    dict_passphrase = {}
    for s in passphrase:
        if s in dict_passphrase:
            dict_passphrase[s] += 1
        else:
            dict_passphrase[s] = 1
    for i in dict_passphrase.values():
        if i != 1:
            return False
            break
    return True

def main():
    with open("passphrases.txt", "r", encoding="utf-8") as fajl:
        passphrases = fajl.read().splitlines()
        fajl.close()
    count = 0
    for s in passphrases:
        if is_passphrase(s):
            count += 1
    print(count)

if __name__ == "__main__":
    main()