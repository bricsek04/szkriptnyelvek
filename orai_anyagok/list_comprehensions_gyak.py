# 20120818d

elso = ['auto', 'villamos', 'metro']
result = [s.upper() + "!" for s in elso]
print(result)

masodik = ['aladar', 'bela', 'cecil']
result = [s.capitalize() for s in masodik]
print(result)

# harmadik
result = [ 0 for n in range(10)]
print(result)

# negyedik
result = [n*2 for n in range(1,11)]
print(result)

otodik = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
result = [int(s) for s in otodik]
print(result)

hatodik = "1234567"
result = [int(c) for c in hatodik]
print(result)

hetedik = 'The quick brown fox jumps over the lazy dog'
result = [len(s) for s in hetedik.split()]
print(result)

nyolcadik = "python is an awesome language"
result = [s[0] for s in nyolcadik.split()]
print(result)

kilencedik = 'The quick brown fox jumps over the lazy dog'
result = [(s, len(s)) for s in kilencedik.split()]
print(result)

# tizedik
result = [i for i in range(10) if i % 2 == 0]
print(result)

# tizenegy
result = [i**2 for i in range(20) if i % 2 == 0]
print(result)

# tizenkettő
result = [i**2 for i in range(20) if str(i**2)[-1] == "4"]
print(result)

# tizenhárom
result = ''.join([chr(i) for i in range(65, 91)])
print(result)

tizennegy = [' apple ', ' banana ', ' kiwi']
result = [s.strip() for s in tizennegy]
print(result)

tizenot = [1, 0, 1, 1, 0, 1, 0, 0]
result = ''.join([str(s) for s in tizenot])
print(result)