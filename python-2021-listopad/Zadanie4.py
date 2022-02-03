import math

def licz(obl_liczba):
    liczba_tekst = str(obl_liczba)
    suma = 0
    for i in range(len(liczba_tekst)):
        suma += int(liczba_tekst[i]) ** 2
    return suma


def licz_wesole4_1(amount):
    arr = []
    liczba = amount
    while liczba != 1:
        arr.append(liczba)
        liczba = licz(liczba)
        for i in range(len(arr)):
            if arr[i] == liczba:
                # print(arr)
                return False
    return (amount, len(arr))


print("4.1")
wyniki4_1 = []
max = 0
for i in range(1, 1001):
    wynik = licz_wesole4_1(i)
    if wynik:
        if wynik[1] > max:
            wyniki4_1 = []
            max = wynik[1]
            wyniki4_1.append(wynik)
        elif wynik[1] == max:
            wyniki4_1.append(wynik)
for x, y in wyniki4_1:
    print(f"{y}\t{x}")

print("4.2")
plik = open("liczby.txt")
wiersze = plik.readlines()
wyniki4_2 = []
for wiersz in wiersze:
    wiersz = wiersz.rstrip()
    if licz_wesole4_1(wiersz):
        wyniki4_2.append(wiersz)
print(len(wyniki4_2))


def licz_wesole4_3(amount):
    arr = []
    liczba = amount
    while liczba != 1:
        arr.append(liczba)
        liczba = licz(liczba)
        for i in range(len(arr)):
            if arr[i] == liczba:
                # print(arr)
                return False
    return True


print("4.3")
ciag = []
naj_ciag = []
for wiersz in wiersze:
    wiersz = wiersz.rstrip()
    if licz_wesole4_3(wiersz):
        ciag.append(wiersz)
    if len(ciag) >= 1:
        if wiersz < ciag[-1]:
            ciag = []
    if licz_wesole4_3(wiersz) == False:
        ciag = []
    if len(ciag) > len(naj_ciag):
        naj_ciag = ciag
print(f"{len(naj_ciag)}\t{naj_ciag[0]}\t{naj_ciag[-1]}")

print("4.4")




def pierwsza(num):
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a = a + 1
    return True


pom_wyniki4_4 = []
wyniki4_4 = []
for wiersz in wiersze:
    wiersz = wiersz.rstrip()
    if licz_wesole4_3(wiersz):
        pom_wyniki4_4.append(wiersz)
for liczba in pom_wyniki4_4:
    liczba = int(liczba)
    if pierwsza(liczba):
        wyniki4_4.append(liczba)
print(len(wyniki4_4))

