def majority_element_two(arr):
    n = len(arr)
    freq = {}
    for x in arr:
        freq[x] = freq.get(x,0)+1

    val = max(freq,key = freq.get)

    if freq[val] > n//3:
        return val
    
arr = [1, 2, 1, 1, 3, 2]
print(majority_element_two(arr))
