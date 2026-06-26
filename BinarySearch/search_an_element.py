def binary_search(arr,target):
     n = len(arr)
     low = 0
     high = n-1
     while low<high:
          mid = (low+high)//2
          if arr[mid] ==target:
               return mid
          if arr[mid]<target:
               low = mid+1
          else:
               high = mid-1
     return -1

arr = [1,2,3,4,5,6]
target = 3
print(binary_search(arr,target))
               
