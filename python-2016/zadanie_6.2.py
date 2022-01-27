file = open("dane_6_2.txt")
lines = file.readlines()


count = 0
for line in lines:
    count+=1
    x = line.split()
    zdanie=[]
    x[0].rstrip()
    for letter in x[0]:
        ascii_letter = ord(letter)
        if len(x)>1:
            for i in range(int(x[1])):
                if ascii_letter==65:
                    ascii_letter=90
                else:   
                    ascii_letter-=1
        ascii_letter = chr(ascii_letter)
        zdanie.append(ascii_letter)
    print(''.join(zdanie))
print(f"odszyfrowane slowa {count}")

    
