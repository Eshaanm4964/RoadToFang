def leaders_in_an_array(nums):
        ans = []
        
        if not nums:
            return ans
        
        max_val = nums[-1]
        ans.append(nums[-1])
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > max_val:
                ans.append(nums[i])
                max_val = nums[i]
        ans.reverse()
        
        return ans

arr = [4, 7, 1, 0]
print(leaders_in_an_array(arr))
