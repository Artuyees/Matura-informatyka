import math


file = open("pary.txt")
lines = file.readlines()
file.close()

def spl(var: str):
    return var.rstrip().split()
lines = list(map(spl, lines))

def isPrime(n):
    s = int(math.sqrt(n))
    for i in range(2, s+1):
        if n % i == 0:
            return False
    return True

def goldbach(n: int):
    if n % 2 != 0:
        return
    num1 = 0
    num2 = 0 
    for i in range(3,n+1):
        diff = n-i
        if diff % 2 == 0 or i % 2 == 0:
            continue
        if not isPrime(diff) or not isPrime(i):
            continue
        if num2-num1 <= diff - i:
            num2=diff
            num1=i
    return(f"{n} {num1} {num2}")



for line in lines:
    result = goldbach(int(line[0]))
    if result:
        print(result)


