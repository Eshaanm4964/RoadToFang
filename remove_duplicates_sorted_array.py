def remove_duplicates_from_sorted_array(arr):
    n = len(arr)
    seen = set()
    result = []
    
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return len(result),result 


arr = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicates_from_sorted_array(arr))