def longest_substring(s):
    n = len(s)
    max_count = 0
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if s[i] != s[j]:
                count+=1
                j+=1
            else:
                count = 0
        max_count = max(count,max_count)
    return max_count
                
s = "abcddabac"
print(longest_substring(s))