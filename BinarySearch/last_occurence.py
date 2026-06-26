def last_occurence(arr,target):
    n = len(arr)
    low = 0
    high = n-1 
    ans = -1
    while low <=high:
        mid = (low+high)//2
        if arr[mid]==target:
            ans = mid
            low = mid +1
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return ans 

arr = [3, 4, 13, 13, 13, 20, 40]
target = 13
print(last_occurence(arr,target))
