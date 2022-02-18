

import math


def is_perfect(n: int):
    s:int = 1
    p = math.ceil(math.sqrt(n))
    for i in range(2,p):
        if n%i == 0:
            s += i + n/i
    if n == p*p: s-=p

    if n==s: return True
    return False

# przykladowe liczby doskonale 6, 28, 496

n = input("Wprowadz liczbe")
n = int(n)

if (is_perfect(n)): print(f"{n} jest doskonala")
else: print(f"{n} nie jest doskonala")