def floor(arr,x):
    n = len(arr)
    low = 0 
    high = n-1 
    ans = -1 
    while low <=high:
        mid = (low+high)//2
        if arr[mid]<=x:
            ans = arr[mid] 
            low = mid+1
        else:
            high = mid-1
    return ans 

def ceil(arr,x):
    n = len(arr)
    low = 0
    high = n-1 
    ans = -1 
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >=x:
            ans = arr[mid]
            high = mid-1
        else:
            low = mid+1
    return ans 



arr = [3, 4, 4, 7, 8, 10]
x = 5
print(floor(arr,x))


arr = [3, 4, 4, 7, 8, 10]
x = 5
print(ceil(arr,x))