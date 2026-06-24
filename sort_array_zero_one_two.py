#def sort_array_zero_ones_two(arr):
 #   n = len(arr)
  #  for i in range(n):
   #     for j in range(0,n-i-1):
    #        if arr[j]>arr[j+1]:
     #           arr[j],arr[j+1] = arr[j+1],arr[j]
    #return arr

#better

def sort_ones_zeroes_twos(arr):
    n = len(arr)
    largest = arr[0]
    for x in arr:
        if x > largest:
            largest = x
            x,largest = largest,x
    return arr

arr = [0,0,1,1,1]
arr = [0,1,2,0,1,0,2]
#print(sort_array_zero_ones_two(arr))
print(sort_ones_zeroes_twos(arr))