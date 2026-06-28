def find_sqrt(n):
    if n<2:
          return n
    left = 0
    right = n//2
    ans = 0
    while left <=right:
        mid = (left + right)//2
        if mid * mid <= n:
                ans = mid
                left = mid + 1
        else:
                right = mid - 1
    return ans


n = 36
print(find_sqrt(n))
