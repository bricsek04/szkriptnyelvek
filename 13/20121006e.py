# Haladó rendezés

def elso_key(x):
    return x[3]

def masodik_key(x):
    return int(x.split(':')[0])

def harmadik_key(x):
    return x[1]

def elso_feladat():
    data = [ 
        (1, 'Albany', 'NY', 162692),
        (121, 'Wyoming', 'NY', 8722),
        (3, 'Allegany', 'NY', 11986),
        (123, 'Yates', 'NY', 5094)
    ]
    print(sorted(data, key=elso_key))

def masodik_feladat():
    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(sorted(users, key=masodik_key, reverse=True))

def harmadik_feladat():
    matrix = [ [2, 6], [1, 3], [5, 4] ]
    print(sorted(matrix, key=harmadik_key))

def main():
    elso_feladat()
    masodik_feladat()
    harmadik_feladat()

if __name__ == "__main__":
    main()