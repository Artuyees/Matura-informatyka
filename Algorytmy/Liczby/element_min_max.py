# Najczesciej pojawiajace sie zagadnienie na maturze.
# zlozonosc O(n)

def min_val(arr: list):
    if len(arr) == 0:
        return
    min_value = arr[0]
    for i in arr:
        if i<min_value:
            min_value = i
    return min_value

def max_val(arr: list):
    if len(arr) == 0:
        return
    min_value = arr[0]
    for i in arr:
        if i>min_value:
            min_value = i
    return min_value




lista = [3,4,5,6,7,8,312412,65,11,21,2]


print(f"min, max: {min_val(lista)}, {max_val(lista)}")


