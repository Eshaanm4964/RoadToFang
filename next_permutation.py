def next_permutation(arr):
    n = len(arr)
    last = arr[-1]
    for i in range(n-1):
        arr[i] = arr[i+1]
    last = arr[-1]
    return arr

arr = [1,2,3]
print(next_permutation(arr))
