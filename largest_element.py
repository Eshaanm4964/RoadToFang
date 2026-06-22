
def largest_element(arr):
    n = len(arr)
    largest = arr[0]
    for x in arr:
        if x >largest:
            largest = x
    return largest


arr = [10,3,2,14,4]
print(largest_element(arr))