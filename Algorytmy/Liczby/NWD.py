# algorytm wyszukujacy najwiekszy wspolny dzielnik. 

import math


def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a


first = input("wprowadz pierwsza liczbe: ")
second = input("wprowadz druga liczbe: ")

first, second = int(first), int(second)
print(nwd_i(first, second))


#Na praktyce nie pisac takiego algorytmu.
#Wbudowana biblioteka math zawiera funkcje math.gcd(pierwszaCyfra, drugaCyfra).

# Pog
print(math.gcd(first, second ))