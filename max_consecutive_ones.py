def max_consecutive_ones(arr):
    count = 0
    max_count = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            count = 0

        max_count = max(count, max_count)

    return max_count