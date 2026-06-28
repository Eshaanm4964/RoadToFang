def minimum_rotated_sorted_array(arr):
    n = len(arr)
    low = 0
    high = n-1
    ans = -1
    while low<high:
        mid = (low+high)//2
        if arr[mid]>arr[high]:
            low = mid+1
        else:
            high = mid 
    return arr[mid]

arr = [4,5,6,7,0,1,2,3]
print(minimum_rotated_sorted_array(arr))
       
        