file = open("instrukcje.txt")
lines = file.readlines()

def transform(var: str):
    return (var.strip())




lines_t = map(transform, lines)
lines_t = list(lines_t)


# 4.1
tekst = []
for line in lines_t:
    split = line.split()
    if split[0] == "DOPISZ":
        tekst.append(split[1])
    if split[0] == "ZMIEN": 
        tekst[len(tekst)-1]=split[1]
    if split[0] == "USUN":
        tekst.pop()
    if split[0] == "PRZESUN":
        index = tekst.index(split[1])
        numer = ord(tekst[index])
        if numer == 90:
            numer = 65
        else:
            numer+=1
        tekst[index]=chr(numer)
odp = "".join(tekst)

print(f"4,1: {len(odp)}")


# 4.2
max = 0 
current_max = 0
max_instruction = lines_t[0].split()[0]
current_instruction = lines_t[0].split()[0]
for i in lines_t:
    split = i.split()
    if split[0] == current_instruction: 
        current_max+=1
    else:
        current_max = 1
        current_instruction = split[0]
    if current_max > max:
        max = current_max
        max_instruction = current_instruction
print(f"4.2: {max_instruction} {max}")

#4.3
letters = {}
for i in lines_t:
    split = i.split()
    if split[0] == "DOPISZ":
        if split[1] in (letters):
            letters[split[1]] +=1
        else:
            letters[split[1]] = 1
max_letter=""
max_count=0
for i in letters:
     if letters[i]>max_count:
         max_letter=i
         max_count=letters[i]
print(max_letter, max_count)
# 4.4

print(f"4.4: {odp}")
