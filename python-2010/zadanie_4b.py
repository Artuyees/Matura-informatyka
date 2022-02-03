file = open("anagram.txt")
lines = file.readlines()

lista = []
result = []
for line in lines:
    line = line.rstrip()
    line_split = line.split()
    if all(len(line_split[0])==len(i) for i in line_split):
        lista.append(line_split)
for word_other in lista:
    if all(sorted(i)==sorted(word_other[0]) for i in word_other):
        result.append(word_other)

for odp in result:
    print(odp)