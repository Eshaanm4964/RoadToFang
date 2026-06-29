def longest_consecutive_sequence(arr):
    if not arr:
        return 0

    arr.sort()

    longest = 1
    current = 1

    for i in range(1, len(arr)):
        # Ignore duplicates
        if arr[i] == arr[i - 1]:
            continue

        # Consecutive element
        elif arr[i] == arr[i - 1] + 1:
            current += 1

        # Sequence breaks
        else:
            longest = max(longest, current)
            current = 1

    longest = max(longest, current)

    return longest


arr = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_sequence(arr))