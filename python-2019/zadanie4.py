import math


file = open("liczby.txt")
lines = file.readlines()
file.close()

def clean(i: str):
    return i.strip()

lines = list(map(int,map(clean, lines)))

#4.1
multi_of_3 = []
multi=0
while True:
    result = 3**multi
    if result>100000:
        break
    multi_of_3.append(result)
    multi+=1

count = 0
for line in lines:
    if line in multi_of_3:
        count+=1
print(f"4.1: {count}")

#4.2
def silnia(x: int):
    result = 1
    if x == 0:
        return 1
    for i in range(1,x+1):
        result*=i
    return result

wynik = []
for line in lines:
    line_str = str(line)
    sum = 0
    for letter in line_str:
        sum += silnia(int(letter))
    if sum==line:
        wynik.append(line)
print(f"4.2:  \n{wynik}")

#4.3 Ciezki algorytm, -5 punktów by było XD. algorytm: http://pythonwszkole.pl/python-na-maturze/matura-2019-zadanie-4/
# math.gcd() Zwraca najwiekszy wspolny dzielnik dwóch liczb
longest = []
arr = []
number = lines[0]
last = 0
for i in lines:
    if len(arr) == 0:
        arr.append(i)
    else:
        number = arr[0]
        for x in arr:
            number = math.gcd(number, x)
        if math.gcd(number, i) != 1:
            arr.append(i)
        else:
            last = arr[-1]
            if len(arr) > len(longest):
                longest = arr.copy()
                arr = [i]
            else:
                arr = [i]
            if math.gcd(i, last) > 1:
                arr = [last, i]
NWD = longest[0]
for x in longest:
    NWD = math.gcd(NWD, x)
print(f"4.4: {longest[0]}, {len(longest)}, {NWD}")