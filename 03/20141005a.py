# valami_1 or valami_2 or … valami_N

import sys

def main():
    inp = input("Do you really want to quit [y/Y/yes]? ")
    if inp in ['y', 'Y', 'yes']:  #if inp == 'y' or inp == 'Y' or inp == 'yes':    # <- egyszerűbben?
        print('bye')
        sys.exit(0)
    # for any other input:
    else:
        print('The show goes on...')
        main()

##############################################################################

if __name__ == "__main__":
    main()