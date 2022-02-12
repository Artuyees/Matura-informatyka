import math


piksele = []
file = open("dane.txt")
lines = file.readlines()
for line in lines:
    temp = line.rstrip().split(" ")
    piksele.append([int(x) for x in temp])
#6.1
min_br = 258
max_br = 0
for line in lines:
    line = line.rstrip()
    pixels = line.split(" ")
    
    for pixel in pixels:
        if int(pixel) > int(max_br):
            max_br = pixel
        if int(pixel) < int(min_br):
            min_br = pixel
print(f"min_br: {min_br}, max_br: {max_br}")

#6.2
count = 0
for line in lines:
    line = line.rstrip()
    pixels = line.split(" ")
    if pixels != pixels[::-1]:
        count+=1
print(f"Minimalna ilosc wierszy: {count}")


#6.3                           
def czy_kontrastujace(pix1, pix2):
    if pix1 - pix2 > 128 or pix2 - pix1 > 128:
        return True
    return False

max_x = 320
max_y = 200
odp = 0
for y in range(len(piksele)):

    line = piksele[y]

    for x in range(len(piksele[0])):
        linia = line[x]

        left_index = x - 1
        if not left_index < 0:
            left = line[left_index]
            if czy_kontrastujace(linia, left):
                odp += 1
                continue
    
        right_index = x + 1
        if not right_index >= max_x:
            right = line[right_index]
            if czy_kontrastujace(linia, right):
                odp += 1
                continue

        up_index = y - 1
        if not up_index < 0:
            up = piksele[up_index][x]
            if czy_kontrastujace(linia, up):
                odp += 1
                continue

        down_index = y + 1
        if not down_index >= max_y:
            down = piksele[down_index][x]
            if czy_kontrastujace(linia, down):
                odp += 1
                continue
print(f'ilosc Kontrastujacych: {odp}')
file.close()

#6.4


max_dl = 1
for k in range(320):
    dl = 1
    for w in range(1,200):
        if piksele[w][k]==piksele[w-1][k]:
            dl+=1
        else:
            dl=1
        if dl>max_dl:
            max_dl = dl
print(f"Max_dlugosc: {max_dl}")