def linear_search(arr,target):
    n = len(arr)
    for i in range(len(arr)):
        if arr[i]==target:
            return True,i
    return -1

arr = [10,8,9,45,66,0]
target = 0
print(linear_search(arr,target))
        
            