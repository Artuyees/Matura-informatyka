file = open("dane.txt")
lines = file.readlines()

#6.1

count = 0
for line in lines:
    line = line.strip()
    line = str(line)
    if (line[0] == line[len(line)-1]): count += 1
print(f"6.1: {count}")

#6.2

count2 = 0
for line in lines:
    line = line.strip()
    line = int(line, 8)     #z ósemkowego na dziesiętny
    line = str(line)
    if (line[0] == line[len(line)-1]): count2 += 1
print(f"6.2: {count2}")

#6.3
count3 = 0
min = 20000000001
max = 0
for line in lines:
    line = line.strip()
    line = str(line)
    if all(line[i]<=line[i+1] for i in range(len(line)-1)):
        count3 +=1
        line = int(line)
        if line < min:
            min = line
        elif line > max:
            max = line
print (f"6.3:ile {count3} min:{min} max:{max}")


