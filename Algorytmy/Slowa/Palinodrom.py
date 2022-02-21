
# Wersja na praktyke XD

def pali(word: str):
    if word == word[::-1]: 
        return True
    else: return False 

# wersja bardziej złożona
def pali_2(word: str):
    i: int = 0
    j: int = len(word)-1
    while(i<j):
        if word[i]!=word[j]:
            return False
        i+=1
        j-=1
    return True



input_word = input("Wprowadz slowo: ")

print(f"Czy jest palindromem?: {pali(input_word)}")