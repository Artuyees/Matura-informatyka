def szyfruj(word: str, key: int):
    word_1 = word.strip().upper()
    word_2 = ''
    for letter in word_1:
        ascii_letter = ord(letter) 
        for i in range(key):
            ascii_letter+=1
            if  ascii_letter == 90:
                ascii_letter -= 26
        word_2 += chr(ascii_letter)
    return word_2

def odszyfruj(word: str, key: int):
    word_1 = word.strip().upper()
    word_2 = ''
    for letter in word_1:
        ascii_letter = ord(letter) 
        for i in range(key):
            ascii_letter-=1
            if  ascii_letter == 64:
                ascii_letter += 26
        word_2 += chr(ascii_letter)
    return word_2

# KONIEC ALGORYTMU 
input_word  = input("Wprowadz tekst: ")
checkbox = input("zaszyfrowac czy odszyfrowac? (1 lub 2): ")

if checkbox == "1":
    print(f"zaszyfrowany tekst: {szyfruj(input_word, 20)}")
else: 
    print(f"odszyfrowany tekst {odszyfruj(input_word, 20)}")