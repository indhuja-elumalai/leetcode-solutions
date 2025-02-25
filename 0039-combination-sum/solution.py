class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        # Backtracking helper function
        def backtrack(start, target, current_combination):
            if target == 0:
                result.append(current_combination)
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    # Explore the combination including candidates[i]
                    backtrack(i, target - candidates[i], current_combination + [candidates[i]])
        
        # Start the backtracking with an empty combination and the full target
        backtrack(0, target, [])
        
        return result

