def findPeakElement(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid + 1]:
            high = mid
        else:
            low = mid + 1
    return low

nums = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(nums))