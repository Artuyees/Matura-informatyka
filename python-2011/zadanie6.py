file = open("liczby.txt")
lines = file.readlines()


countA = 0
max = int(lines[0], 2)
max_2 = 0
countC = 0
sumC = 0
for line in lines:
    line10 = int(line, 2)
    
    # a)

    if line10 % 2 == 0 :
        countA+=1

    if line10 > max:
        max = line10
        max_2 = line
    if len(str(line)) == 10:
        countC +=1
        sumC += line10
sumC = bin(sumC) 
    
print(f"6.A) {countA}")
print(f"6.B) Najwieksza liczba: {max}, {max_2}")
print(f"6.C) Tyle liczb: {countC}, i ich suma wynosi {sumC[2:]}")