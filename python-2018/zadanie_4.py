
file = open("sygnaly.txt")
lines = file.readlines()
file.close()

def clean(i: str):
    return i.strip()


lines = list(map(clean, lines))
#4.1
word = ""
for line in lines[39::40]:
    word+=line[9]
print(f"4.1: {word}")
 
#4.2
dictionary = {}
for line in lines:
    if line in dictionary:
        continue
    dictionary[line] = 0
    for i in range(0, len(line)):
        if line.find(line[i], i+1, len(line)) < 0:
            dictionary[line]+=1
max = 0 
max_item = ''
for item in dictionary:
    if dictionary[item] > max:
        max_item = item
        max = dictionary[item]
print(f"4.2: {max_item} {max}") 


#4.3
# Tragicznie podpunkt. Przyklad.txt wychodzi dobrze biorąc pod uwagę tylko sąsiadujące litery co nie zostało sprecyzowane. CKE w pełnej klasie.

arr = []


# 2 pkt za taki algorytm (Tylko sasiadujace wyrazy):
""" 
for line in lines:
    is_not_away = True
    for i in range(1,len(line)):
        if not is_not_away:
            continue
        if abs((ord(line[i]) - ord(line[i-1])))>10:
            is_not_away = False
    if is_not_away:
        arr.append(line) 
"""

# 4 punkty za taki (Wszystkie wyrazy):
for line in lines:
    max = 0
    min = 1000
    for letter in line:
        if ord(letter)>max: 
            max=ord(letter)
        if ord(letter)<min: 
            min=ord(letter)
        diff = max-min
    if diff<=10: arr.append(line)
# Odpowiedz ledwo mieszczaca sie na 2 kartkach A4 XD.

print("4.3:")
for line in arr:
    print(line)