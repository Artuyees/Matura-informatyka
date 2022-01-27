file = open("dane_6_3.txt")
lines = file.readlines()


for line in lines:
    x = line.split()
    x[0].rstrip()
    x[1].rstrip()
    lista=[]
    for i in range(len(x[0])):
        key = 0
        first = ord(x[0][i])
        second = ord(x[1][i])
        while first != second:
            key+=1
            if first==90:
                first=65
            else:   
                first+=1
        lista.append(key)
    # Sprawdz czy wszystkie liczby w liscie sa rowne liczbie o indeksie 0
    # Czyli czy wszystkie są takie same
    if not all(lista[0]==lista[i] for i in range(len(lista))):
        print(line)

            
    
