def loop(freq, debug=False):
    if debug:
        print ("Ciklus kezdete!")
    for i in range(1, freq+1):
        print(i)
    if debug:
        print ("Ciklius vége!")



def main():
    loop(5, debug=True)

if __name__ == "__main__":
    main()