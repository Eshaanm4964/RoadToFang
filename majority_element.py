def majority_element(arr):
    n = len(arr)
    freq = {}
    for x in arr:
        freq[x] = freq.get(x,0)+1
    majority = max(freq)
    half = len(arr)//2
    if majority > half:
        return x
    return -1

arr = [7, 0, 0, 1, 7, 7, 2, 7, 7]
print(majority_element(arr))