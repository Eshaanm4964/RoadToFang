#The array has been rotated at some random point 
#arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6], k = 3

def rotated_Sorted_array_two(arr,k):
    n = len(arr)
    low = 0 
    high = n-1 
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == k:
            return True 
        elif arr[low]<=arr[mid]:
            if arr[low]<=k<arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid]<k<=arr[high]:
                low = mid+1
            else:
                high = mid-1
    return False

arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
k = 10
print(rotated_Sorted_array_two(arr,k))
