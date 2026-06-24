def union_two_sorted_arrays(arr1,arr2):
    result = []
    seen = set()
    for x in arr1 or arr2:
        if x in arr1:
            seen.add(x) 
        if x in arr2:
            seen.add(x)
        result.append(x)
    return result 

arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]

print(union_two_sorted_arrays(arr1,arr2))