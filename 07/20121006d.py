# Fájlkezelés

with open("string1.py", 'r') as be, open ("string1_clean.py", 'w') as ki:
    for line in be:
        if not line.lstrip().startswith('#'):
            ki.write(line)
