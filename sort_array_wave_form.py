def wave_form(arr):
    n = len(arr)

    for i in range(0, n - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


arr = [1, 2, 3, 4, 5]
print(wave_form(arr))