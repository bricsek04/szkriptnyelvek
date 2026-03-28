# Zárójelek

def zarojel(kifejezes):
    stack = []
    pairs = {')' : '(', ']':'[', '}':'{'}
    for c in kifejezes:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack or stack.pop() != pairs[c]:
                return False
    return len(stack) == 0

def main():
    print(zarojel("((5+3)*2+1)"))
    print(zarojel("{[(3+1)+2]+}"))
    print(zarojel("(3+{1-1)}"))
    print(zarojel("[1+1]+(2*2)-{3/3}"))
    print(zarojel("(({[(((1)-2)+3)-3]/3}-3)"))

if __name__ == "__main__":
    main()