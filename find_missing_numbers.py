def find_missing_numbers(arr):
    n = len(arr)+1
    total_sum = sum(arr)
    actual = n*(n+1)//2
    return actual - total_sum

arr = [1,2,3,4,5,7,8,9]
print(find_missing_numbers(arr))