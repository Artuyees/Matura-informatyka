def szyfruj(word: str, key: int):
    word_1 = word.strip()
    word_2 = ''
    for letter in word_1:
        ascii_letter = ord(letter) 
        for i in range(key):
            ascii_letter+=1
            if  ascii_letter == 90:
                ascii_letter -= 26
        word_2 += chr(ascii_letter)
    return word_2

x = szyfruj("OKOKOK", 20)
print(x)