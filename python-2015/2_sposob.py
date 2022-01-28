
file = open("Matura-informatyka-2022\Python-2015\liczby.txt")
rows = file.readlines()

# 4.1

""" 
Z treści zadania A: Podaj, ile jest słów w pliku 
slowa.txt, w których liczba zer jest większa od liczby jedynek.
 """

more_zero_count = 0
for row in rows:
    zero_count = 0
    one_count = 0
    for number in str(row):
        if number == "0":
            zero_count += 1
        elif number == "1":
            one_count += 1
    if zero_count > one_count:
        more_zero_count += 1
print(f"4.1:\t{more_zero_count}")

# 4.2 

""" 
Podaj, ile jest słów składających się z dokładnie dwóch niepustych bloków: pierwszego
składającego się samych zer i drugiego składającego się z samych jedynek 
"""

# Nie zamieniamy na int jak w poprzednim rozwiazaniu

DIV_2_COUNT = 0
DIV_8_COUNT = 0
for row in rows:
    div_by_8 = str(row[-4:len(row)-1])
    div_by_2 = str(row[-2:len(row)-1])
    if div_by_8 == "000":   
        DIV_8_COUNT +=1
    if div_by_2 == "0": 
        DIV_2_COUNT +=1
print(f"4.2:\tby 2: {DIV_2_COUNT}\tby 8: {DIV_8_COUNT} ")


#4.3

"""
Podaj długość najdłuższego bloku złożonego z samych zer pojawiającego się w słowach
w pliku slowa.txt. Wypisz wszystkie słowa z tego pliku, które zawierają taki najdłuższy
blok złożony z samych zer.
Przykład:
Dla zestawu słów:
100010000100
001
000
10101001110000
000011
Wynikami są liczba 4 oraz pogrubione słowa.  
"""


min_number = 1000
min_index = 0
max_number = 0
max_index = 0
i = 0
for row in rows:
    i+=1
    number = int(row, 2)
    if number < min_number:
        min_number = number
        min_index = rows.index(row)
    if number > max_number:
        max_number = number
        max_index = rows.index(row)


# minimum i maksimum +1 bo chodzi o wiersz a nie o indeks
# Nieuważne czytanie i 6pkt stracone
print(f"4.3:\tmin: {min_index+1}, max: {max_index+1}")

file.close()
