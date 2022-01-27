file = open("liczby.txt")
rows = file.readlines()

# 4.1

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

div_2_count = 0
div_8_count = 0

for row in rows:
    number = int(row, 2)
    if number % 2 == 0:
        div_2_count += 1
    if number % 8 == 0:
        div_8_count += 1
print(f"4.2:\tby 2: {div_2_count}\tby 8: {div_8_count} ")


# 4.3
# jesli 1 indeks jest najmniejszy to jest mniejszy od podstawowej wartosci 
# jesli którykolwiek inny to napewno jest mniejszy także od pierwszego
min_number = int(rows[0], 2)+1
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
