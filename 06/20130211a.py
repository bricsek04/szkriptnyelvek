# Anagramma

def normalize(string):
    return ''.join(string.lower().split())

def is_anagramma(szo1, szo2):
    dict_szo1 = {}
    dict_szo2 = {}
    for c in normalize(szo1):
        if c in dict_szo1:
            dict_szo1[c] +=1
        else:
            dict_szo1[c] = 1
    for c in normalize(szo2):
        if c in dict_szo2:
            dict_szo2[c] +=1
        else:
            dict_szo2[c] = 1
    return(dict_szo1 == dict_szo2)

def is_anagramma_v2(szo1, szo2):
    return sorted(list(normalize(szo2))) == sorted(list(normalize(szo1)))


def main():
    print(normalize("Clint Eastwood"))
    print(is_anagramma("listen", "silent"))
    print(is_anagramma_v2("listen", "silnet"))

if __name__ == "__main__":
    main()