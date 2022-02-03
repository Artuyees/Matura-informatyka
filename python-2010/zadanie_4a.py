file = open("anagram.txt")
lines = file.readlines()

lista = []
for line in lines:
    line = line.rstrip()
    line_split = line.split()
    if all(len(line_split[0])==len(i) for i in line_split):
        lista.append(line_split)
for i in lista:
    print(i)