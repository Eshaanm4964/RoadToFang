def left_rotate_by_one(arr):
    last = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr[-1] = last
    return arr

arr = [0,1,2,3,4]
print(left_rotate_by_one(arr))
