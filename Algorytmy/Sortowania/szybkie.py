# p - poczatek, k - koniec, s - srodek. CKE zazwyczaj nazywa to w taki sposob


def partition(arr, p, k):
    i = (p-1)        
    pivot = arr[k]     
 
    for j in range(p, k):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[k] = arr[k], arr[i+1]
    return (i+1)

 
 
def quickSort(arr, p, k):
    if len(arr) == 1:
        return arr
    if p < k:
        s = partition(arr, p, k)
        quickSort(arr, p, s-1)
        quickSort(arr, s+1, k)
 
 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print(f"Posortowana tablica: {arr}")

 