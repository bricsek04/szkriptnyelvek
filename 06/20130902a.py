# Medián
def median(numbers):
    rendezett = sorted(numbers)
    n = len(rendezett)
    
    kozepso_index = n // 2
    
    if n % 2 != 0:
        return rendezett[kozepso_index]
    else:
        felso_kozep = rendezett[kozepso_index]
        also_kozep = rendezett[kozepso_index - 1]
        return (also_kozep + felso_kozep) / 2

def main():
    l1 = [1, 2, 3, 4, 5]
    l2 = [3, 1, 2, 5, 3]
    l3 = [1, 300, 2, 200, 1]
    l4 = [3, 6, 20, 99, 10, 15]
    print(median(l1))
    print(median(l2))
    print(median(l3))
    print(median(l4))

if __name__ == "__main__":
    main()