def max_product(arr):
    n = len(arr)
    arr.sort()
    return arr[-1]*arr[-2]*arr[-3]

arr = [10,3,5,6,20]
print(max_product(arr))
