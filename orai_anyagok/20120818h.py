osszeg = 0
with open("szamok.txt", "r") as szamok:
    for s in szamok:
        osszeg += int(s)
print(str(osszeg)[:10])