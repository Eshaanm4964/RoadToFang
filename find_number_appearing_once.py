def find_number_appearing_once(arr):
    n = len(arr)
    if len(arr)<1:
        return -1

    freq = {}
    for x in arr:
        freq[x] = freq.get(x,0)+1

    if freq[x]==1:
        return x
    
    return -1

arr = [2,2,1,1,5]
print(find_number_appearing_once(arr))
