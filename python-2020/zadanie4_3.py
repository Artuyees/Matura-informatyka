import math


file = open("pary.txt")
lines = file.readlines()
file.close()

def spl(var: str):
    return var.rstrip().split()
lines = list(map(spl, lines))

lines_check=[]
result=[]

for line in lines:
    if int(line[0]) == len(line[1]):
        lines_check.append(line)

min=100
for line in lines_check:
    if int(line[0])<int(min):
        min=line[0]
support_array=[]
for line in lines_check:
    if int(line[0])==int(min):
        support_array.append(line[1])
support_array.sort()

for line in lines_check:
    if line[1] == support_array[0] and int(line[0]) == int(min):
        print(line)
        break
