class Solution:
    def permuteUnique(self,nums):
        result = []
        nums.sort()  # Sort to handle duplicates
    
        def backtrack(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return
        
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
            
                used[i] = True
                backtrack(path + [nums[i]], used)  # Append and recurse
                used[i] = False
    
        used = [False] * len(nums)
        backtrack([], used)
    
        return result


