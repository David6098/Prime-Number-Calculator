import json


primzahlen = []
n = 1
z = 100
while True:
    n =n +1
    primzahlen.append(n)
    for a in primzahlen:
        if a*a <= n:
            b = n//a
            if b*a == n:
                primzahlen.pop(-1)
                break
    if len(primzahlen) == z:
        z = z + 100
        with open('data.json', 'w') as f:
            json.dump(primzahlen, f)