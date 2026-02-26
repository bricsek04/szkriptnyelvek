# Sztring tisztítása

def string_clean(s):
    return s.replace(' ', '').replace('\n', '')

def main():
    print(string_clean('192.20.246.138:\n 6666'))
    print(string_clean('206.130.99.82:\n8080'))

if __name__ == "__main__":
    main()