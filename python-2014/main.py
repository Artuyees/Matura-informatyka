from unittest import skip


file = open("NAPIS.TXT")
rows = file.readlines()


#5.1
count = 0
for row in rows:
    is_prime = True
    sum = 0
    for number in str(row.strip()):
        ascii_number = ord(number)
        sum += ascii_number
    for i in range(2,sum):
        if sum % i == 0:
            is_prime = False

    if is_prime: count += 1 
print(f"5.1: {count}")
 

 #5.2

arr = []
for row in rows:
    if all(ord(row[i])<ord(row[i+1]) for i in range(len(row.rstrip()) - 1)):
        arr.append(row)
        
print(f"5.2: {arr}")
 


 #5.3

all_words={}

for row in rows:
    if row not in all_words:
        all_words[row] = 1
    else:
        all_words[row] +=1

list_words = []
for word in all_words:
    if all_words[word] > 1:
        list_words.append(word)
print(f"5.3 {list_words}")

