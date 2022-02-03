file = open("sz.txt")
keys_file = open("klucze2.txt")
lines = file.readlines()
keys = keys_file.readlines()
file.close()
keys_file.close()


lista = []
for line in lines:
    decrypted_word=""
    x = lines.index(line)
    key = keys[x]
    key = key.rstrip()
    line = line.rstrip()
    index = 0 
    for letter in line:
        if index>(len(key)-1):
            index = 0
        number = ord(letter)
        key_letter = key[index]
        key_of_number = ord(key_letter)-64
        result = number - key_of_number
        if result < 65:
            result = result + 26
        decrypted_word += chr(result)
        index+=1
    lista.append(decrypted_word)
print(lista)