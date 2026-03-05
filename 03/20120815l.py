# Rejtélyes üzenet

def decode_message(szoveg):
    abc    = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    offset = "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB"
    erdemeny = ""
    for char in szoveg:
        if char in abc:
            erdemeny += offset[abc.index(char)] # index vs find -> index: ValueError, find: -1.
        else:
            erdemeny += char
    return erdemeny

def main():
    encoded_message = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb""".strip()
    print(decode_message(encoded_message))
    

if __name__ == "__main__":
    main()