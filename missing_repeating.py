def missing_repeating(arr):
    n = len(arr)
    result = []
    seen = set()

    for x in arr:
        if x in seen:
            result.append(x)      
        else:
            seen.add(x)

    actual = sum(arr)
    expected = n * (n + 1) // 2

    missing = result[0] - (actual - expected)

    result.append(missing)

    return result


arr = [3, 1, 3]
print(missing_repeating(arr))