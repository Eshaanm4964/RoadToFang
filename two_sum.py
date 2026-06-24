def two_sum(arr,target):
    seen = set()
    for x in arr:
        if target - x in arr:
            return True
    return False

arr = [2,6,5,8,11]
target = 14
print(two_sum(arr, target))