
import math


arr = []
n = input("Wprowadz liczbe:")
n= int(n)
pierw = math.sqrt(n)


k=2
while n > 1 and k<=pierw:
    while n % k==0:
            arr.append(k)
            n/=k
    k+=1

print(arr)