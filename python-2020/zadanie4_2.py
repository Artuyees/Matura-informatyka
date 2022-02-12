
file = open("pary.txt")
lines = file.readlines()
file.close()
def spl(var: str):
    return var.rstrip().split()
lines = list(map(spl, lines))

for line in lines:
    word = line[1]
    max_word = ""
    count=0
    current_word = word[0]
    for letter in word:
        if letter == current_word[0] or letter==word[0]:
           count += 1
           current_word += letter
        else:
            count = 1
            current_word = letter
        if len(current_word)>len(max_word):
            max_word=current_word
    print(max_word, len(max_word))        

