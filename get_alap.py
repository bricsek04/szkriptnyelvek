import os

def create_file(filename, content):
    if os.path.isfile(filename):
        print("A fájl már létezik!")
    else:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print("Elkészült a fájl!")
        f.close()

def main():
    py_template = """#!/usr/bin/env python3

def main():
    print('Py3')

##############################################################################

if __name__ == "__main__":
    main()
"""

    c_template = """#include <stdio.h>

int main() {
    printf("Hello C\\n");
    return 0;
}
"""

    while True:
        print("-" * 27)
        print("Create an empty source file")
        print("-" * 27)
        print("1) Python [py]")
        print("2) C      [c]")
        print("q) quit")
        
        choice = input("> ").strip().lower()

        if choice == '1':
            create_file("alap.py", py_template)
            break
        elif choice == '2':
            create_file("alap.c", c_template)
            break
        elif choice == 'q':
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás, próbáld újra!")

if __name__ == "__main__":
    main()