def max_product(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr, arr[-1]*arr[-2]*arr[-3]

arr = [10,3,5,6,20]
print(max_product(arr))
