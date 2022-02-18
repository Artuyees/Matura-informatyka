def fib(n):
    if n == 0: return 0 
    elif n == 1: return 1 
    p, w = 0, 1     # pierwsze 2 cyfry ciagu
    for i in range(n-1):    
        p, w = w, p+w   
    return w

n = input("Wprowadz numer liczby w ciagu: ")
n = int(n)

print(fib(n))