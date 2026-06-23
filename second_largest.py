def second_largest(arr):
    n = len(arr)
    largest = second = float("-inf")
    for x in arr:
        if x >largest:
            second = largest
            largest = x
        if x<largest and x>second:
            second = x
    return second

arr = [10,9,11,6,7]
print(second_largest(arr))