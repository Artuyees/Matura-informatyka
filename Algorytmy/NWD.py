# algorytm wyszukujacy najwiekszy wspolny dzielnik. 

def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a


first = input("wprowadz pierwsza liczbe: ")
second = input("wprowadz druga liczbe: ")

first, second = int(first), int(second)
print(nwd_i(first, second))