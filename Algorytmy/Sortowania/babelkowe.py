
def sort(arr: list):

    n = len(arr)
    
    while n > 1:
        #Dopoki rzeczy sa zamieniane WYKONUJ
        zamien = False
        for l in range(0, n-1):
            # Jesli dana wartosc w tabeli jest wieksza od nastepnej, ZAMIEN
            # jezeli nastepne takze jest wieksza to tez ZAMIEN, tak dlugo az bedzie wieksza od kazdej poprzedniej.
            if arr[l] > arr[l+1]:                      
                arr[l], arr[l+1] = arr[l+1], arr[l]
                zamien = True
        
        n -= 1
        #print(arr) #Jesli chcemy wypisac kazdy krok.
        if zamien == False: break
        
    return arr


#przykladowa tablica: 
arr = [3,6,21,83452,784,21,9,34,8,4,2,9,4,2,7,23,7]


print(f"nieposortowana: {arr}")
print(f"posortowana: {sort(arr)}")



