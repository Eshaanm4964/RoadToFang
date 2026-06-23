def move_zeroes_to_end(arr):
    n = len(arr)
    temp = []
    for i in range(len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])

    for i in range(len(arr)):
        if arr[i]==0:
            temp.append(arr[i])

    return temp 

arr = [0,1,2,0,4,5,0]
print(move_zeroes_to_end(arr))