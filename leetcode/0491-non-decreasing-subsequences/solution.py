class Solution:
    def findSubsequences(self, nums):
        def backtrack(i, path, seen):
            if len(path) > 1 and tuple(path) not in seen:
                res.append(path[:])
                seen.add(tuple(path))
            for j in range(i, len(nums)):
                if not path or nums[j] >= path[-1]:
                    path.append(nums[j])
                    backtrack(j + 1, path, seen)
                    path.pop()

        res, seen = [], set()
        backtrack(0, [], seen)
        return res

