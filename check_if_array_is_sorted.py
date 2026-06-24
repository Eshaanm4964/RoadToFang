def check_array_is_sorted(arr):
    n = len(arr)
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            return True 
    return False
arr = [1,2,3,4,5,6]
print(check_array_is_sorted(arr))