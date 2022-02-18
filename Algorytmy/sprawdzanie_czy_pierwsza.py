

def is_prime(n: int):
    if n<2: return False
    for i in range(2,n):
        if n%i==0: return False
    return True


n = input("Wprowadz liczbe")
n = int(n)

if(is_prime(n)):    print(f"{n} jest pierwsza")
else:   print(f"{n} nie jest pierwsza")